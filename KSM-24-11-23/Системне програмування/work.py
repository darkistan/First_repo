import threading
import time


def work(number: int):
    for i in range(1, 6):
        print(f"Потік {number} крок {i}")
        time.sleep(0.5)


def main():
    t1 = threading.Thread(target=work, args=(1,))
    t2 = threading.Thread(target=work, args=(2,))

    t1.start()
    t2.start()

    print("Потоки запущено")

    # Щоб програма не завершилась раніше, ніж потоки закінчать роботу
    t1.join()
    t2.join()

    print("Потоки завершили роботу")


if __name__ == "__main__":
    main()