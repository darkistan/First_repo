while True:
    try:
        size = int(input("Введіть розмір масиву: "))
        if size <= 0:
            print("Розмір має бути більше 0!")
            continue
        break
    except ValueError:
        print("Будь ласка, введіть ціле число.")

array = []
for i in range(size):
    while True:
        try:
            val = int(input(f"Елемент {i}: "))
            array.append(val)
            break
        except ValueError:
            print("Введіть ціле число!")

print("Ваш масив:", array)
