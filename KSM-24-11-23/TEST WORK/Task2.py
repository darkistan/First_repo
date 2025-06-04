import datetime

while True:
    print("\nМеню:")
    print("1. Привітатися")
    print("2. Надрукувати дату")
    print("3. Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print("Привіт, користувачу!")
    elif choice == "2":
        print("Поточна дата і час:", datetime.datetime.now())
    elif choice == "3":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір! Спробуйте ще раз.")
