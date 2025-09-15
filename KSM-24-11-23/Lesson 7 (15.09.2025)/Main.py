import json
import threading
import time

STATE_FILE = "lamp_state.json"

class Lamp:
    def __init__(self, is_on=False, brightness=100, color="white"):
        self.is_on = bool(is_on)
        self.brightness = int(brightness)
        self.color = str(color)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, value):
        # перевірка коректності: 0..100
        value = int(value)
        if value < 0 or value > 100:
            raise ValueError("Яскравість має бути від 0 до 100.")
        self.brightness = value

    def set_color(self, color_name):
        color_name = str(color_name).strip().lower()
        if color_name == "":
            raise ValueError("Колір не може бути пустим.")
        self.color = color_name

    def status_str(self):
        state = "Увімкнено" if self.is_on else "Вимкнено"
        return f"Стан: {state} | Яскравість: {self.brightness} | Колір: {self.color}"

    def to_dict(self):
        return {"is_on": self.is_on, "brightness": self.brightness, "color": self.color}

    @staticmethod
    def from_dict(d):
        return Lamp(is_on=d.get("is_on", False),
                    brightness=d.get("brightness", 100),
                    color=d.get("color", "white"))

def save_state(lamp, filename=STATE_FILE):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(lamp.to_dict(), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Не вдалося зберегти стан:", e)

def load_state(filename=STATE_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Lamp.from_dict(data)
    except FileNotFoundError:
        return None
    except Exception as e:
        print("Помилка завантаження стану:", e)
        return None

# --- Авто-режими ---
def auto_color_cycle(lamp, stop_event, interval=2):
    colors = ["white", "yellow", "blue", "red", "green", "purple"]
    idx = 0
    while not stop_event.is_set():
        lamp.set_color(colors[idx % len(colors)])
        lamp.turn_on()
        idx += 1
        # чекати інтервал, але з можливістю швидкого завершення
        for _ in range(int(interval*10)):
            if stop_event.is_set():
                break
            time.sleep(0.1)

def auto_brightness_pulse(lamp, stop_event, min_b=10, max_b=100, step=10, interval=1):
    # пульс яскравості
    b = min_b
    up = True
    while not stop_event.is_set():
        lamp.set_brightness(b)
        lamp.turn_on()
        if up:
            b += step
            if b >= max_b:
                b = max_b
                up = False
        else:
            b -= step
            if b <= min_b:
                b = min_b
                up = True
        for _ in range(int(interval*10)):
            if stop_event.is_set():
                break
            time.sleep(0.1)

def start_thread(target, args):
    t = threading.Thread(target=target, args=args, daemon=True)
    t.start()
    return t

def main():
    # завантажити попередній стан (якщо є)
    lamp = load_state() or Lamp()

    # події для зупинки авто-режимів
    stop_auto = threading.Event()
    auto_threads = []  

    while True:
        print("\n=== Меню дистанційного керування світильником ===")
        print("1 - Увімкнути світильник")
        print("2 - Вимкнути світильник")
        print("3 - Змінити яскравість (0-100)")
        print("4 - Змінити колір (наприклад: white, yellow, blue, red)")
        print("5 - Переглянути поточний стан")
        print("6 - Автоматичний режим (вкл/викл)")
        print("7 - Зберегти стан")
        print("8 - Завершити програму")
        choice = input("Виберіть дію (1-8): ").strip()

        if choice == "1":
            lamp.turn_on()
            print("Світильник увімкнено.")
        elif choice == "2":
            lamp.turn_off()
            print("Світильник вимкнено.")
        elif choice == "3":
            val = input("Введіть яскравість (0-100): ").strip()
            try:
                lamp.set_brightness(int(val))
                print("Яскравість змінена.")
            except Exception as e:
                print("Помилка:", e)
        elif choice == "4":
            col = input("Введіть назву кольору (наприклад white, yellow, blue, red): ").strip()
            try:
                lamp.set_color(col)
                print("Колір змінено.")
            except Exception as e:
                print("Помилка:", e)
        elif choice == "5":
            print(lamp.status_str())
        elif choice == "6":
            # меню авто-режиму
            print("\n-- Автоматичний режим --")
            print("a - Запустити циклічну зміну кольорів (кольори міняються кожні N секунд)")
            print("b - Запустити автоматичне регулювання яскравості (пульсація)")
            print("c - Зупинити всі авто-режими")
            sub = input("Виберіть (a/b/c): ").strip().lower()
            if sub == "a":
                if any(t.is_alive() for t in auto_threads):
                    print("Уже запущено авто-режим. Зупиніться перед запуском іншого.")
                else:
                    sec = input("Інтервал між кольорами в секундах (наприклад 2): ").strip()
                    try:
                        sec_f = float(sec)
                        stop_auto.clear()
                        t = start_thread(auto_color_cycle, (lamp, stop_auto, sec_f))
                        auto_threads = [t]
                        print("Авто-режим зміни кольорів запущено.")
                    except Exception as e:
                        print("Помилка:", e)
            elif sub == "b":
                if any(t.is_alive() for t in auto_threads):
                    print("Уже запущено авто-режим. Зупиніться перед запуском іншого.")
                else:
                    interval = input("Інтервал між кроками в секундах (наприклад 1): ").strip()
                    try:
                        interval_f = float(interval)
                        stop_auto.clear()
                        t = start_thread(auto_brightness_pulse, (lamp, stop_auto, 10, 100, 10, interval_f))
                        auto_threads = [t]
                        print("Авто-режим пульсації яскравості запущено.")
                    except Exception as e:
                        print("Помилка:", e)
            elif sub == "c":
                if any(t.is_alive() for t in auto_threads):
                    stop_auto.set()
                    # зачекати трохи, щоб потоки зупинились
                    time.sleep(0.2)
                    auto_threads = []
                    stop_auto.clear()
                    print("Усі авто-режими зупинені.")
                else:
                    print("Авто-режими не запущені.")
            else:
                print("Невірний вибір в авто-режимі.")
        elif choice == "7":
            save_state(lamp)
            print(f"Стан збережено у файлі '{STATE_FILE}'.")
        elif choice == "8":
            # перед виходом зупинити авто-режими і зберегти стан
            if any(t.is_alive() for t in auto_threads):
                stop_auto.set()
                time.sleep(0.2)
            save_state(lamp)
            print("Стан збережено. Вихід.")
            break
        else:
            print("Невірна команда. Введіть число від 1 до 8.")

if __name__ == "__main__":
    main()
