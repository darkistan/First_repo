
import datetime

def show_menu():
    print("\n=== ГОЛОВНЕ МЕНЮ ===")
    print("1. Показати привітання")
    print("2. Порахувати суму двох чисел")
    print("3. Показати поточний час")
    print("0. Вийти")

def run_menu():
    while True:
        show_menu()
        choice = input("Введіть пункт меню: ")

        match choice:
            case "1":
                print("Привіт! Радий тебе бачити.")
            case "2":
                try:
                    a = float(input("Введіть перше число: "))
                    b = float(input("Введіть друге число: "))
                    print(f"Сума: {a + b}")
                except ValueError:
                    print("Помилка: введіть правильні числа.")
            case "3":
                now = datetime.datetime.now()
                print("Поточний час:", now.strftime("%Y-%m-%d %H:%M:%S"))
            case "0":
                print("Вихід з програми...")
                break
            case _:
                print("Невідомий пункт меню. Спробуйте ще раз.")


run_menu()

