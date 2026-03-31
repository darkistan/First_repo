import os

handles = []

try:
    for i in range(1000):
        fd = os.open("leak.txt", os.O_WRONLY | os.O_CREAT)
        handles.append(fd)

    print("1000 дескрипторів відкрито.")
    input("Натисніть Enter, щоб завершити програму...")
except OSError as e:
    print(f"Помилка: {e}")
