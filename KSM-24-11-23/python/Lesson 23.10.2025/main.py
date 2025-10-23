# Метод бісекції для чисельного розв'язання рівняння f(x) = 0

import math  # для використання у f(x)

def f(x):
    # Приклад функції: cos(x) - x = 0
    return math.cos(x) - x

# Ввід даних користувачем
# a, b — межі відрізка; eps — точність; max_iter — максимальна кількість ітерацій
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
eps = float(input("Введіть eps: "))
max_iter = int(input("Введіть max_iter: "))

# Перевірка умови зміни знаку
f_a = f(a)
f_b = f(b)

if f_a * f_b >= 0:
    print("Помилка: на [a, b] має бути зміна знаку (f(a) * f(b) < 0).")
else:
    it = 0
    # Основний цикл бісекції
    while (b - a) / 2.0 > eps and it < max_iter:
        mid = (a + b) / 2.0
        f_mid = f(mid)

        # Вибір підвідрізка зі зміною знаку
        if f_a * f_mid <= 0:
            b = mid
            f_b = f_mid
        else:
            a = mid
            f_a = f_mid

        it += 1

    # Результати
    root = (a + b) / 2.0
    err_est = (b - a) / 2.0
    f_root = f(root)

    print("Наближений корінь:", root)
    print("Кількість ітерацій:", it)
    print("Оцінка похибки (верхня межа):", err_est)
    print("Значення f(root):", f_root)
