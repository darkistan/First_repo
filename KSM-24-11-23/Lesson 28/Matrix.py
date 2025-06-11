import random

def matrix_game():
    print("🔵🟢🔴 Вітаю, Обраний. Ти опинишся в цифровому лабіринті Матриці...")
    print("Щоб війти, пройди три випробування. Твоє здоров'я: 3 ❤️")
    
    health = 3
    score = 0

    # --- Рівень 1: Вибір пігулки ---
    print("\n🔑 Рівень 1: Вибір пігулки")
    pills = ["червона", "синя", "зелена"]
    correct_pill = random.choice(pills)

    while True:
        choice = input("Обери пігулку (червона/синя/зелена): ").strip().lower()
        if choice == correct_pill:
            print("✅ Ти зробив правильний вибір! Переходимо далі...")
            score += 1
            break
        elif choice not in pills:
            print("⚠️ Невідома пігулка. Обери одну з: червона, синя, зелена.")
        else:
            print("❌ Пастка! Спробуй ще раз.")

    # --- Рівень 2: Математична загадка ---
    print("\n🧠 Рівень 2: Математична загадка")
    math_question = "12 + 7 * 2"
    correct_answer = eval(math_question)

    while True:
        try:
            user_answer = int(input(f"Обчисли: {math_question} = "))
            if user_answer == correct_answer:
                print("✅ Правильна відповідь!")
                score += 1
                break
            else:
                health -= 1
                print(f"❌ Неправильно. Агент Сміт атакує! Здоров'я: {health} ❤️")
                if health == 0:
                    print("💀 Тебе спіймали агенти. Кінець гри.")
                    return
        except ValueError:
            print("Введи ціле число.")

    # --- Рівень 3: Шифрований код ---
    print("\n🔐 Рівень 3: Шифрований код")
    
    decoded = "".join(chr(ord(c) - 1) for c in encoded)

    while True:
        user_input = input("Введи розшифроване слово: ").strip().lower()
        if user_input == decoded:
            print("✅ Правильно! Ти знайшов вхід.")
            score += 1
            break
        else:
            health -= 1
            print(f"❌ Невірно. Здоров'я: {health} ❤️")
            if health == 0:
                print("💀 Зашифрований код виявився фатальним. Кінець гри.")
                return

    # --- Фінал ---
    print("\n🎉 Фінал")
    if score == 3:
        print("🚀 Ти потрапив у матрицю! Вітаю, НЕО.")
    elif score == 2:
        print("😮 Ти дійшов до кінця, але з втратами...")
    else:
        print("🤕 Ти вижив, але ледве. Матриця ще попереду.")

    print(f"✅ Вдалих рішень: {score} / 3")

# Запуск гри
if __name__ == "__main__":
    matrix_game()
