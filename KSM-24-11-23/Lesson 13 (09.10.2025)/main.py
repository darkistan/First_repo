# Імпортуємо модуль datetime для роботи з датами
import datetime

# Виводимо назву програми
print("Програма 'Відлік днів до свята'")
print("--------------------------------")

# Користувач вводить поточну дату
day = int(input("Введіть поточний день: "))
month = int(input("Введіть поточний місяць (числом): "))
year = int(input("Введіть поточний рік: "))

# Створюємо об'єкт дати для поточної дати
current_date = datetime.date(year, month, day)

# Користувач вводить дату свята
print("\nВведіть дату вашого свята:")
holiday_day = int(input("День свята: "))
holiday_month = int(input("Місяць свята (числом): "))
holiday_name = input("Назва свята: ")

# Створюємо дату свята у поточному році
holiday_date = datetime.date(year, holiday_month, holiday_day)

# Якщо свято вже минуло — рахуємо до свята у наступному році
if holiday_date < current_date:
    holiday_date = datetime.date(year + 1, holiday_month, holiday_day)

# Обчислюємо різницю між датами
difference = holiday_date - current_date
days_left = difference.days

# Виводимо результат
print(f"\nДо свята '{holiday_name}' залишилось {days_left} днів!")

# Жартівливе повідомлення
print(f"Готуйся до {holiday_name.lower()}! 🎉")
