# Завдання 2. Пошук email у тексті
# Знайти всі email у тексті (регулярним виразом).
# Вивести список знайдених адрес і кількість унікальних.

import re

def find_emails(text):
    """
    Знаходить email-адреси в тексті і повертає список знайдених адрес.
    """
    pattern = r'[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}'
    # Повертаємо всі знайдені (ігноруємо регістр)
    return re.findall(pattern, text, flags=re.IGNORECASE)

def main():
    # Коротка інструкція для користувача
    print("Завдання 2: Пошук email у тексті")
    sample = "Приклад: info@mail.com, support@university.edu.ua, olexandr.petrenko+it@gmail.com"
    text = input("Введіть текст для пошуку email (натисніть Enter для прикладу): ")
    if not text:
        text = sample

    found = find_emails(text)
    unique = set(found)

    print("\nРезультат (Завдання 2):")
    print("Знайдені адреси:", found)
    print("Кількість знайдених:", len(found))
    print("Кількість унікальних адрес:", len(unique))
    print("Унікальні адреси:", list(unique))

if __name__ == "__main__":
    main()
