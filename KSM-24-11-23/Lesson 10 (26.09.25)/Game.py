
from copy import deepcopy

# ====== Базові утиліти координат ======

#  перетворюю алгебраїчну нотацію 'e2' у індекси масиву [рядок, стовпець]
def alg_to_rc(s: str):
    if len(s) != 2 or s[0] < 'a' or s[0] > 'h' or s[1] < '1' or s[1] > '8':
        return None
    col = ord(s[0]) - ord('a')      # 'a' -> 0 ... 'h' -> 7
    row = 8 - int(s[1])             # '8' зверху -> 0 ... '1' знизу -> 7
    return (row, col)

#  зручна перевірка меж дошки
def in_bounds(r, c):
    return 0 <= r < 8 and 0 <= c < 8

# ====== Класи фігур ======

class Piece:
    #базовий клас фігури — колір, символ, прапорець чи рухалась
    def __init__(self, color):
        self.color = color  # 'white' або 'black'
        self.has_moved = False

    @property
    def symbol(self):
        return '?'  # буде перевизначено в підкласах

    def char(self):
        # виводжу великі літери для білих, малі — для чорних
        return self.symbol if self.color == 'white' else self.symbol.lower()

    def allowed_moves(self, board, r, c):
        # абстрактний метод у підкласах
        return []


class Pawn(Piece):
    @property
    def symbol(self):
        return 'P'

    def allowed_moves(self, board, r, c):
        moves = []
        # напрям — білі вгору (до менших r), чорні вниз (до більших r)
        dir = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1

        # крок уперед 1
        nr, nc = r + dir, c
        if in_bounds(nr, nc) and board.get(nr, nc) is None:
            moves.append((nr, nc))
            # крок уперед 2 зі стартової, якщо обидві клітинки вільні
            nr2 = r + 2 * dir
            if r == start_row and in_bounds(nr2, nc) and board.get(nr2, nc) is None:
                moves.append((nr2, nc))

        # діагоналі для взяття
        for dc in (-1, 1):
            nr, nc = r + dir, c + dc
            if in_bounds(nr, nc):
                target = board.get(nr, nc)
                if target is not None and target.color != self.color:
                    moves.append((nr, nc))
        # en passant не реалізую — його немає у вимогах
        return moves


class Rook(Piece):
    @property
    def symbol(self):
        return 'R'

    def allowed_moves(self, board, r, c):
        moves = []
        #  4 напрямки по прямих до першої перепони
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            while in_bounds(nr, nc):
                if board.get(nr, nc) is None:
                    moves.append((nr, nc))
                else:
                    if board.get(nr, nc).color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves


class Knight(Piece):
    @property
    def symbol(self):
        return 'N'

    def allowed_moves(self, board, r, c):
        moves = []
        for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc):
                target = board.get(nr, nc)
                if target is None or target.color != self.color:
                    moves.append((nr, nc))
        return moves


class Bishop(Piece):
    @property
    def symbol(self):
        return 'B'

    def allowed_moves(self, board, r, c):
        moves = []
        #  4 діагоналі до першої перепони
        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            nr, nc = r + dr, c + dc
            while in_bounds(nr, nc):
                if board.get(nr, nc) is None:
                    moves.append((nr, nc))
                else:
                    if board.get(nr, nc).color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves


class Queen(Piece):
    @property
    def symbol(self):
        return 'Q'

    def allowed_moves(self, board, r, c):
        #  ферзь = тура + слон
        return Rook.allowed_moves(self, board, r, c) + Bishop.allowed_moves(self, board, r, c)


class King(Piece):
    @property
    def symbol(self):
        return 'K'

    def allowed_moves(self, board, r, c):
        moves = []
        #  крок на 1 у будь-який бік
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc):
                    target = board.get(nr, nc)
                    if target is None or target.color != self.color:
                        moves.append((nr, nc))

        #  додаю рокіровку (перевірка базових умов тут)
        if not self.has_moved:
            # важливо: король не повинен бути під шахом прямо зараз
            if not board.is_in_check(self.color):
                row = 7 if self.color == 'white' else 0
                # коротка рокіровка: e->g (колонка 4 -> 6)
                if r == row and c == 4:
                    # клітинки між королем та турою: f(5), g(6)
                    if board.get(row, 5) is None and board.get(row, 6) is None:
                        rook = board.get(row, 7)
                        if isinstance(rook, Rook) and rook.color == self.color and not rook.has_moved:
                            # жодна з клітинок e,f,g не під боєм суперника
                            if (not board.is_square_attacked((row, 5), board.opponent(self.color))
                                and not board.is_square_attacked((row, 6), board.opponent(self.color))):
                                moves.append((row, 6))
                # довга рокіровка: e->c (4 -> 2), пусті: b(1), c(2), d(3)
                if r == row and c == 4:
                    if board.get(row, 3) is None and board.get(row, 2) is None and board.get(row, 1) is None:
                        rook = board.get(row, 0)
                        if isinstance(rook, Rook) and rook.color == self.color and not rook.has_moved:
                            if (not board.is_square_attacked((row, 3), board.opponent(self.color))
                                and not board.is_square_attacked((row, 2), board.opponent(self.color))):
                                moves.append((row, 2))
        return moves

# ====== Дошка ======

class Board:
    # зберігаю 8x8 масив з None або екземплярами фігур
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial()

    def clone(self):
        #  глибока копія для симуляції ходів
        return deepcopy(self)

    def setup_initial(self):
        # стандартна початкова позиція
        # чорні зверху (рядок 0 і 1)
        self.grid[0] = [
            Rook('black'), Knight('black'), Bishop('black'), Queen('black'),
            King('black'), Bishop('black'), Knight('black'), Rook('black')
        ]
        self.grid[1] = [Pawn('black') for _ in range(8)]
        # порожні ряди
        for r in range(2, 6):
            self.grid[r] = [None for _ in range(8)]
        # білі знизу (рядок 7 і 6)
        self.grid[6] = [Pawn('white') for _ in range(8)]
        self.grid[7] = [
            Rook('white'), Knight('white'), Bishop('white'), Queen('white'),
            King('white'), Bishop('white'), Knight('white'), Rook('white')
        ]

    def display(self):
        # виводжу з верхнього (8) до нижнього (1) як у прикладі
        for r in range(8):
            row_chars = []
            for c in range(8):
                piece = self.grid[r][c]
                row_chars.append(piece.char() if piece else '.')
            print(' '.join(row_chars))
        # пустий рядок для читабельності
        print()

    def get(self, r, c):
        return self.grid[r][c]

    def set(self, r, c, piece):
        self.grid[r][c] = piece

    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                p = self.get(r, c)
                if isinstance(p, King) and p.color == color:
                    return (r, c)
        return None

    def opponent(self, color):
        return 'white' if color == 'black' else 'black'

    # перевірка, чи клітинка під боєм певного кольору (без рекурсії з allowed_moves)
    def is_square_attacked(self, sq, by_color):
        r, c = sq

        # 1) атаки пішаками
        pawn_dir = -1 if by_color == 'white' else 1
        for dc in (-1, 1):
            rr, cc = r + pawn_dir, c + dc
            if in_bounds(rr, cc):
                p = self.get(rr, cc)
                if isinstance(p, Pawn) and p.color == by_color:
                    return True

        # 2) атаки конем
        for dr, dc in [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
            rr, cc = r + dr, c + dc
            if in_bounds(rr, cc):
                p = self.get(rr, cc)
                if isinstance(p, Knight) and p.color == by_color:
                    return True

        # 3) лінійні/діагональні (тура/слон/ферзь)
        # тура/ферзь
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            rr, cc = r + dr, c + dc
            while in_bounds(rr, cc):
                p = self.get(rr, cc)
                if p is None:
                    rr += dr; cc += dc
                    continue
                if p.color == by_color and (isinstance(p, Rook) or isinstance(p, Queen)):
                    return True
                break
        # по діагоналях: слон/ферзь
        for dr, dc in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            rr, cc = r + dr, c + dc
            while in_bounds(rr, cc):
                p = self.get(rr, cc)
                if p is None:
                    rr += dr; cc += dc
                    continue
                if p.color == by_color and (isinstance(p, Bishop) or isinstance(p, Queen)):
                    return True
                break

        # 4) сусідній король
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr == 0 and dc == 0: continue
                rr, cc = r + dr, c + dc
                if in_bounds(rr, cc):
                    p = self.get(rr, cc)
                    if isinstance(p, King) and p.color == by_color:
                        return True

        return False

    def is_in_check(self, color):
        # перевірка шаху — чи поле короля під боєм суперника
        king_pos = self.find_king(color)
        if not king_pos:
            return False
        return self.is_square_attacked(king_pos, self.opponent(color))

    #  виконання ходу (припускаю, що перевірка легальності вже зроблена)
    # повертаю взяту фігуру (щоб можна було дебажити за потреби)
    def move_piece(self, sr, sc, tr, tc):
        piece = self.get(sr, sc)
        captured = self.get(tr, tc)

        # спеціальна логіка для рокіровки (король рухається на 2 клітинки)
        if isinstance(piece, King) and abs(tc - sc) == 2:
            row = sr
            if tc == 6:  # коротка: e->g, тура: h->f
                rook = self.get(row, 7)
                self.set(row, 5, rook)
                self.set(row, 7, None)
                if rook: rook.has_moved = True
            elif tc == 2:  # довга: e->c, тура: a->d
                rook = self.get(row, 0)
                self.set(row, 3, rook)
                self.set(row, 0, None)
                if rook: rook.has_moved = True

        self.set(tr, tc, piece)
        self.set(sr, sc, None)
        if piece:
            piece.has_moved = True

        # промоція пішака в ферзя автоматично при досягненні останнього ряду
        if isinstance(piece, Pawn):
            if piece.color == 'white' and tr == 0:
                self.set(tr, tc, Queen('white'))
            elif piece.color == 'black' and tr == 7:
                self.set(tr, tc, Queen('black'))

        return captured

    # генерація принаймні одного легального ходу для певного кольору
    def has_any_legal_move(self, color):
        for r in range(8):
            for c in range(8):
                p = self.get(r, c)
                if p is None or p.color != color:
                    continue
                for (tr, tc) in p.allowed_moves(self, r, c):
                    test = self.clone()
                    test.move_piece(r, c, tr, tc)
                    if not test.is_in_check(color):
                        return True
        return False

# ====== Клас гри ======

class Game:
    # керую циклом гри, перевіркою ходів, шахом/матом і чергою ходу
    def __init__(self):
        self.board = Board()
        self.current = 'white'  # білі ходять першими

    def parse_move(self, line):
        # очікую формат "e2 e4"; також допускаю "resign" для здачі
        line = line.strip()
        if line.lower() == 'resign':
            return 'resign', None, None, None
        parts = line.split()
        if len(parts) != 2:
            return 'error', None, None, None
        s, t = parts
        src = alg_to_rc(s)
        dst = alg_to_rc(t)
        if src is None or dst is None:
            return 'error', None, None, None
        return 'ok', src[0], src[1], dst

    def is_legal(self, sr, sc, tr, tc):
        piece = self.board.get(sr, sc)
        if piece is None:
            return False, "Порожня клітинка на старті."
        if piece.color != self.current:
            return False, "Це не ваша фігура."
        if sr == tr and sc == tc:
            return False, "Хід у ту ж клітинку."
        # псевдолегальні ходи фігури
        moves = piece.allowed_moves(self.board, sr, sc)
        if (tr, tc) not in moves:
            return False, "Фігура так не ходить."
        # заборонено залишати свого короля під шахом
        test = self.board.clone()
        test.move_piece(sr, sc, tr, tc)
        if test.is_in_check(self.current):
            return False, "Після ходу ваш король під шахом."
        return True, ""

    def switch(self):
        self.current = self.board.opponent(self.current)

    def is_checkmate_against(self, color):
        # мат: король під шахом і немає жодного легального ходу
        if not self.board.is_in_check(color):
            return False
        return not self.board.has_any_legal_move(color)

    def run(self):
        # головний цикл
        print("Початкова позиція:")
        self.board.display()

        while True:
            side_name = "Білий хід" if self.current == 'white' else "Чорний хід"
            print(side_name, "(введіть рух, напр. 'e2 e4', або 'resign' щоб здатися):")
            line = input("> ")

            status, sr, sc, dst = self.parse_move(line)
            if status == 'resign':
                winner = "Чорні" if self.current == 'white' else "Білі"
                print(f"Гравець здався. Перемогли {winner}.")
                break
            if status == 'error':
                print("Невірний формат. Приклад: e2 e4")
                continue

            tr, tc = dst
            ok, msg = self.is_legal(sr, sc, tr, tc)
            if not ok:
                print("Неможливий хід:", msg)
                continue

            # виконуємо хід
            self.board.move_piece(sr, sc, tr, tc)
            self.board.display()

            # перевірка на мат супернику
            opp = self.board.opponent(self.current)
            if self.is_checkmate_against(opp):
                print("Мат! Перемога для", "білих." if self.current == 'white' else "чорних.")
                break

            # просто повідомлення про шах (не завершення)
            if self.board.is_in_check(opp):
                print("Шах", "чорному королю!" if opp == 'black' else "білому королю!")

            # передаємо хід
            self.switch()

# ====== Запуск гри ======

if __name__ == "__main__":
    Game().run()
