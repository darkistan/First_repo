import math

f = input("введіть назву фігури: ")

if f == "коло":
    try:
        r = float(input("Введіть радіус: "))
        if r > 0:
            print("Площа кола =", math.pi * r ** 2)
        else:
            print("Помилка, радіус не може бути менше або рівний нулю")
    except ValueError:
        print("Некоректне число")

elif f == "прямокутник":
    try:
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        if a > 0 and b > 0:
            print("Площа прямокутника =", a * b)
        else:
            print("Помилка, сторони не можуть бути менше або рівні нулю")
    except ValueError:
        print("Некоректне число")

elif f == "трикутник":
    try:
        a = float(input("Основа a: "))
        h = float(input("Висота h: "))
        if a > 0 and h > 0:
            print("Площа трикутника =", 0.5 * a * h)
        else:
            print("Помилка, основа та висота повинні бути додатні")
    except ValueError:
        print("Некоректне число")

elif f == "трапеція":
    try:
        a = float(input("Основа a: "))
        b = float(input("Основа b: "))
        h = float(input("Висота h: "))
        if a > 0 and b > 0 and h > 0:
            print("Площа трапеції =", (a + b) / 2 * h)
        else:
            print("Помилка, основи та висота повинні бути додатні")
    except ValueError:
        print("Некоректне число")

else:
    print("Невідома фігура")
