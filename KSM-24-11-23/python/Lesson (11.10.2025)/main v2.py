def gauss(A, b):
    # Кількість рівнянь (тобто кількість рядків у матриці A)
    n = len(b)

    # === Формування розширеної матриці [A | b] ===
    for i in range(n):
        A[i].append(b[i])

    def print_augmented(step):
        print(f"Крок {step}:")
        for row in A:
            print(row)
        print()

    # === Прямий хід методу Гауса ===
    for i in range(n):
        # --- Знаходимо головний елемент (півод) ---
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]

        # --- Ділимо рядок на головний елемент ---
        pivot = A[i][i]

        # Перевірка вироджених випадків
        if pivot == 0:
            coeffs_zero = all(A[i][j] == 0 for j in range(n))
            if coeffs_zero and A[i][n] != 0:
                raise ValueError("Система не має розв’язків")
            if coeffs_zero and A[i][n] == 0:
                raise ValueError("Система має нескінченно багато розв’язків")
            raise ValueError("Система не має єдиного розв’язку")

        for j in range(i, n + 1):
            A[i][j] /= pivot

        # --- Виключення змінної з інших рядків ---
        for r in range(n):
            if r != i:
                factor = A[r][i]
                for j in range(i, n + 1):
                    A[r][j] -= factor * A[i][j]

        # Вивід розширеної матриці після кроку прямого ходу
        print_augmented(i + 1)

    # === Отримання результату ===
    x = [A[i][-1] for i in range(n)]
    return x


# === Приклад використання ===
A = [
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
]

b = [8.0, -11.0, -3.0]

solution = gauss(A, b)
print("Розв’язок системи:", solution)
