import os

text = "Hello from Python Handle!\n"

try:
    fd = os.open("example.txt", os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    os.write(fd, text.encode("utf-8"))
    os.close(fd)
    print("Файл успішно створено та записано.")
except OSError as e:
    print(f"Помилка створення або запису файлу: {e}")
