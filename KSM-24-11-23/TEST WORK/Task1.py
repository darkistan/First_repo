# Завдання 1: Запит числа і перевірка, чи воно невід’ємне
while True:
    try:
        number = int(input("Введіть число: "))
        if number < 0:
            print("Виявлено від'ємне число")
            continue  # "goto" назад
        break
    except ValueError:
        print("Будь ласка, введіть ціле число.")
print("Прийнято число:", number)
