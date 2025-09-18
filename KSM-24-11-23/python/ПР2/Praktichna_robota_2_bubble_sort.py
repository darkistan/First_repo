# Практична робота №2 — сортування бульбашкою
import random
from typing import List

def bubble_sort(numbers: List[int], ascending: bool = True) -> List[int]:
    
    n = len(numbers)  # кількість елементів у списку

    # Зовнішній цикл — виконуємо n-1 проходів (після кожного проходу один елемент "спливає" на своє місце)
    for i in range(n - 1):
        # Внутрішній цикл — проходимо по неперевіреним парам:
        # останні i елементів вже на своїх місцях, тому йдемо до n-1-i
        for j in range(n - 1 - i):
            # Порівнюємо сусідні елементи numbers[j] і numbers[j+1]
            if ascending:
                # Для сортування за зростанням: якщо лівий більше — міняємо їх місцями
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            else:
                # Для сортування за спаданням: якщо лівий менший — міняємо їх місцями
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Повертаємо відсортований список (той самий об'єкт, що й в аргументі)
    return numbers

# Приклад використання:
if __name__ == "__main__":
    # Створимо випадковий список для демонстрації
    random.seed(42)
    data = [random.randint(0, 100) for _ in range(10)]
    print("Початковий список:", data)

    # Сортування за зростанням
    bubble_sort(data, ascending=True)
    print("Відсортовано за зростанням:", data)

    # Щоб показати сортування за спаданням — створимо новий список
    data2 = [random.randint(0, 100) for _ in range(10)]
    print("Початковий список 2:", data2)
    print("Відсортовано за спаданням:", bubble_sort(data2, ascending=False))
