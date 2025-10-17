#Практична робота №5

#Тема: Використання бібліотеки random для симуляцій. Обробка масивів
#Мета: навчитися створювати випадкові дані, обробляти їх і візуалізувати результати.

import random
import numpy as np
import matplotlib.pyplot as plt

# ===== Завдання 1 =====
# Генерація випадкового списку та операції над ним

# Створюємо список з 20 випадкових чисел від 1 до 100
numbers = [random.randint(1, 100) for _ in range(20)]
print("Початковий список:", numbers)

# Знаходимо статистичні показники
max_num = max(numbers)
min_num = min(numbers)
sum_num = sum(numbers)
avg_num = sum_num / len(numbers)

print(f"Максимальне значення: {max_num}")
print(f"Мінімальне значення: {min_num}")
print(f"Сума елементів: {sum_num}")
print(f"Середнє арифметичне: {avg_num:.2f}")

# Сортування
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Список за зростанням:", ascending)
print("Список за спаданням:", descending)


# ===== Завдання 2 =====
# Обробка масиву даних

# Масив із 15 випадкових чисел від 0 до 50
array = np.random.randint(0, 51, size=15)
print("\nМасив:", array)

# Знаходимо кількість елементів, більших за середнє
mean_val = np.mean(array)
greater_than_mean = np.sum(array > mean_val)

# Сума парних чисел
sum_even = np.sum(array[array % 2 == 0])

# Кількість унікальних елементів
unique_count = len(np.unique(array))

print(f"Середнє значення: {mean_val:.2f}")
print(f"Кількість елементів > середнього: {greater_than_mean}")
print(f"Сума парних чисел: {sum_even}")
print(f"Кількість унікальних елементів: {unique_count}")


# ===== Завдання 3 =====
# Графічне відображення даних

data = [random.randint(1, 50) for _ in range(10)]
indexes = list(range(1, 11))

plt.bar(indexes, data, color='skyblue', edgecolor='black')
plt.title("Стовпчикова діаграма випадкових чисел")
plt.xlabel("Номер елемента")
plt.ylabel("Значення")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# ===== Контрольні питання =====
# 1. Які основні функції модуля random ви знаєте?
#    -> randint(), random(), choice(), sample(), shuffle()

# 2. Чим відрізняється список Python від масиву numpy?
#    -> Список — універсальний контейнер, може містити різні типи даних.
#       Масив numpy — однорідна структура, оптимізована для чисельних обчислень, працює швидше.

# 3. Як можна відсортувати список у порядку спадання?
#    -> Використати sorted(list, reverse=True) або list.sort(reverse=True)

# 4. Які типи графіків можна побудувати за допомогою matplotlib?
#    -> plot (лінійний), bar (стовпчиковий), pie (кругова діаграма),
#       scatter (розсіювання), hist (гістограма) тощо.

# 5. Як знайти унікальні значення в масиві?
#    -> Використати set(list) або np.unique(array)