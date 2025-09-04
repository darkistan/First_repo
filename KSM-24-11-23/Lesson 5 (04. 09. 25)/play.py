import random

# ================================================================
# 🌞 Як я провів літо 🌞
#
# Це літо я провів дуже продуктивно! 
#
# По-перше, я працював на роботі. І працював так старанно, 
# що навіть комп’ютер почав просити відпустку.
#
# 
# А ще я зрозумів головне: літо можна проводити 
# не тільки на морі з коктейлем, а й із ноутбуком і завданнями.  
# Головне — щоб зарплата встигала за цінами на каву.
#
# Висновок: літо вдалося! Робота — була, навчання — було, 
# а відпочинок... ну, він теж десь був, тільки я його ще шукаю 😅
# ================================================================


# Клас для покупки
class Purchase:
    def __init__(self, description, cost):
        self.description = description  # опис покупки
        self.cost = cost                # вартість покупки

# Клас гравця
class Player:
    def __init__(self, budget):
        self.budget = budget    # поточний бюджет
        self.day = 1            # поточний день
        self.purchases = []     # список покупок

    # Виконати покупку
    def make_purchase(self, purchase):
        # Дозволяємо витратити навіть якщо бюджет стане від’ємним
        self.budget -= purchase.cost
        self.purchases.append(purchase)
        print(f"Ви купили: {purchase.description} за {purchase.cost} монет.")

    # Заробити гроші
    def earn_money(self, amount):
        self.budget += amount
        print(f"Ви заробили {amount} монет.")

# Клас гри
class Game:
    def __init__(self, player):
        self.player = player
        self.max_days = 30  # максимальна кількість днів

    # Генерація випадкової математичної задачі
    def generate_math_task(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])
        task = f"{num1} {operator} {num2}"
        answer = eval(task)  # рахуємо правильну відповідь
        return task, answer

    # Основний ігровий цикл
    def play(self):
        while self.player.day <= self.max_days and self.player.budget >= 0:
            print(f"\nДень {self.player.day}: Ваш бюджет = {self.player.budget} монет.")
            print("1. Купити їжу (50 монет)")
            print("2. Розваги (100 монет)")
            print("3. Транспорт (30 монет)")
            print("4. Онлайн-курс (200 монет)")
            print("5. Нічого не робити")
            print("6. Розв'язати математичну задачу (заробити монети)")

            try:
                choice = int(input("Виберіть дію: "))
            except ValueError:
                print("Будь ласка, введіть число від 1 до 6.")
                continue

            if choice == 1:
                purchase = Purchase("Їжа", 50)
                self.player.make_purchase(purchase)
            elif choice == 2:
                purchase = Purchase("Розваги", 100)
                self.player.make_purchase(purchase)
            elif choice == 3:
                purchase = Purchase("Транспорт", 30)
                self.player.make_purchase(purchase)
            elif choice == 4:
                purchase = Purchase("Онлайн-курс", 200)
                self.player.make_purchase(purchase)
            elif choice == 5:
                print("Ви нічого не зробили.")
            elif choice == 6:
                # Генеруємо задачу
                task, correct_answer = self.generate_math_task()
                print(f"Розв'яжіть задачу: {task}")
                try:
                    player_answer = float(input("Ваша відповідь: "))
                    if player_answer == correct_answer:
                        reward = random.randint(50, 150)
                        self.player.earn_money(reward)
                    else:
                        print("Невірна відповідь.")
                except ValueError:
                    print("Будь ласка, введіть число.")
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

            # Після дії збільшуємо день
            self.player.day += 1

            # Якщо гроші в мінусі — гра завершується
            if self.player.budget < 0:
                print("\nВаш бюджет пішов у мінус!")
                break

        self.end_game()

    # Завершення гри
    def end_game(self):
        print(f"\nГра завершена. Ви прожили {self.player.day - 1} днів.")
        print(f"Залишок бюджету: {self.player.budget} монет.")
        print("Повний список витрат:")
        for purchase in self.player.purchases:
            print(f"{purchase.description}: {purchase.cost} монет.")

        # Перевірка виграшу
        if self.player.day > self.max_days and self.player.budget >= 0:
            print("\n🎉 Вітаємо! Ви виграли — прожили всі 30 днів!")
        else:
            print("\n😢 Ви програли — гроші закінчилися раніше.")

# --- Запуск гри ---
player = Player(budget=1000)  # стартовий бюджет
game = Game(player)
game.play()
