side1 = float(input("Введіть першу сторону прямокутника: "))
side2 = float(input("Введіть другу сторону прямокутника: "))

if side1 > 0 and side2 > 0:
    area = side1 * side2
    print(f"Площа прямокутника: {area}")
else:
    print("Одна, або дві сторони не коректні")
