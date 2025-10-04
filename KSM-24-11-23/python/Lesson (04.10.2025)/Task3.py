# Завдання 3. Пошук і нормалізація телефонів
# Знайти всі номери телефонів у тексті і нормалізувати їх до формату +380XXXXXXXXX
# (нормалізація для номерів, що починаються з 0 або 380; інші — INVALID)

import re

def normalize_phone(raw):
    """
    Нормалізує один телефонний рядок до формату +380XXXXXXXXX
    Правила:
      - Якщо після видалення нецифр рядок має 12 цифр і починається з '380' -> +380...
      - Якщо має 10 цифр і починається з '0' -> +380 + останні 9 цифр
      - Інакше -> "INVALID"
    """
    digits = re.sub(r'\D', '', raw)  # залишаємо тільки цифри

    if len(digits) == 12 and digits.startswith('380'):
        return '+' + digits
    if len(digits) == 10 and digits.startswith('0'):
        return '+380' + digits[1:]
    return "INVALID"

def find_phone_like(text):
    """
    Знаходимо фрагменти, які виглядають як телефони,
    потім нормалізуємо кожен знайдений фрагмент.
    Повертаємо список кортежів (оригінал, нормалізований).
    """
    # патерн для телефоноподібних фрагментів (цифри, пробіли, дефіси, дужки, плюс)
    pattern = r'[\+\d][\d\-\s\(\)]{8,}\d'
    candidates = re.findall(pattern, text)
    results = []
    seen = set()
    for c in candidates:
        # Зберігаємо лише унікальні фрагменти в порядку появи
        if c in seen:
            continue
        seen.add(c)
        results.append((c, normalize_phone(c)))
    return results

def main():
    print("Завдання 3: Пошук і нормалізація телефонів")
    sample = "Приклад: +380 (67) 123-45-67, 0501234567, 380671234567, 067-123-45-67"
    text = input("Введіть текст для пошуку телефонів (натисніть Enter для прикладу): ")
    if not text:
        text = sample

    found = find_phone_like(text)

    print("\nРезультат (Завдання 3):")
    if not found:
        print("Телефонів не знайдено.")
    else:
        print("Оригінал  ->  Нормалізовано")
        for orig, norm in found:
            print(f"{orig}  ->  {norm}")

if __name__ == "__main__":
    main()
