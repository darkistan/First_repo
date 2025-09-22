
# Клас Router з потрібними властивостями та методами
class Router:
    def __init__(self, is_on=False, has_internet=False, devices=0, wifi_password="password123"):
        # Стан живлення: увімкнено/вимкнено (True/False)
        self.is_on = is_on
        # Наявність інтернету: підключено/ні (True/False)
        self.has_internet = has_internet
        # Кількість підключених пристроїв (ціле число, не від'ємне)
        self.devices = devices
        # Пароль Wi-Fi (рядок, мінімум 8 символів)
        self.wifi_password = wifi_password

    # --- Методи зміни станів ---

    def turn_on(self):
        # Увімкнути роутер
        self.is_on = True

    def turn_off(self):
        # Вимкнути роутер
        self.is_on = False
        # Логічно: коли роутер вимкнули — інтернету немає і пристрої "відключені"
        self.has_internet = False
        # devices залишимо як лічильник останнього відомого стану 

    def set_internet_state(self, state):
        # Змінити стан підключення до інтернету (True/False)
        # Інтернет можливий лише коли роутер увімкнений
        if not self.is_on and state:
            # Якщо намагаємося увімкнути інтернет, але роутер вимкнений — це некоректно
            return False
        self.has_internet = bool(state)
        return True

    def change_wifi_password(self, new_password):
        # Змінити пароль Wi-Fi (мінімум 8 символів)
        if len(new_password) < 8:
            return False
        self.wifi_password = new_password
        return True

    # --- Допоміжні методи перевірок---

    def is_router_on(self):
        # Повертає True/False — чи увімкнений роутер
        return self.is_on

    def internet_status(self):
        # Повертає True/False — чи є інтернет
        return self.has_internet

    def connected_devices(self):
        # Повертає кількість підключених пристроїв (не від’ємне число)

        if self.devices < 0:
            # Самозахист від некоректного внутрішнього стану
            self.devices = 0
        return self.devices

    def set_devices_count(self, count):
       
        if count < 0:
            return False
        self.devices = int(count)
        return True

    def status_report(self):
        # Текстовий звіт про поточний стан роутера
        lines = []
        lines.append("=== Поточний стан роутера ===")
        lines.append(f"Живлення: {'УВІМКНЕНО' if self.is_on else 'ВИМКНЕНО'}")
        lines.append(f"Інтернет: {'Є підключення' if self.has_internet else 'Немає підключення'}")
        lines.append(f"Підключені пристрої: {self.connected_devices()}")
        # Пароль не виводимо повністю з міркувань безпеки — лише довжину і маску
        masked = '*' * len(self.wifi_password)
        lines.append(f"Пароль Wi-Fi: {masked} (довжина: {len(self.wifi_password)})")
        return "\n".join(lines)

    # --- Режим автотестування ---

    def auto_test(self):
        # Перевіряємо послідовно всі параметри і формуємо зведений звіт
        results = []   # список рядків із результатами кожного тесту
        passed = 0     # лічильник успішних тестів
        total = 0      # загальна кількість тестів

        # Тест 1: стан живлення
        total += 1
        if isinstance(self.is_on, bool):
            results.append("Тест 1 (живлення): УСПІХ — коректний булевий стан.")
            passed += 1
        else:
            results.append("Тест 1 (живлення): ПОМИЛКА — стан має бути булевим True/False.")

        # Тест 2: інтернет
        total += 1
        if isinstance(self.has_internet, bool):
            if not self.is_on and self.has_internet:
                results.append("Тест 2 (інтернет): ПОМИЛКА — при вимкненому роутері інтернет не може бути увімкнено.")
            else:
                results.append("Тест 2 (інтернет): УСПІХ — коректний стан підключення.")
                passed += 1
        else:
            results.append("Тест 2 (інтернет): ПОМИЛКА — стан має бути булевим True/False.")

        # Тест 3: кількість пристроїв — не від’ємна
        total += 1
        if isinstance(self.devices, int) and self.devices >= 0:
            results.append("Тест 3 (пристрої): УСПІХ — кількість не від’ємна.")
            passed += 1
        else:
            results.append("Тест 3 (пристрої): ПОМИЛКА — кількість має бути цілим числом ≥ 0.")

        # Тест 4: пароль — мінімум 8 символів
        total += 1
        if isinstance(self.wifi_password, str) and len(self.wifi_password) >= 8:
            results.append("Тест 4 (пароль): УСПІХ — довжина пароля валідна (≥ 8).")
            passed += 1
        else:
            results.append("Тест 4 (пароль): ПОМИЛКА — пароль короткий (менше 8 символів).")

        # Підсумок
        summary = []
        summary.append("=== Автоматичне тестування роутера ===")
        summary.extend(results)
        summary.append(f"Підсумок: {passed} із {total} тестів пройдено.")
        return "\n".join(summary)


# --- Допоміжні функції для безпечного введення даних ---

def read_menu_choice():
    # Зчитує вибір пункту меню (ціле число). При помилці повертає -1.
    try:
        value = int(input("Ваш вибір: ").strip())
        return value
    except:
        return -1

def read_yes_no(prompt_text):
    # Зчитує відповідь "так/ні" у простому вигляді: т/н (або y/n)
    ans = input(prompt_text).strip().lower()
    # Повертає True для "так", False для "ні"
    return ans in ("t", "т", "y", "yes", "так")


# --- Головне меню програми ---

def main():
    # Створюємо роутер із початковими простими значеннями
    router = Router(
        is_on=False,          # роутер вимкнений
        has_internet=False,   # інтернет відсутній
        devices=2,            # умовно 2 пристрої були підключені
        wifi_password="password123"   # валідний початковий пароль
    )

    # Безкінечний цикл меню до виходу користувача
    while True:
        print("\n================ МЕНЮ ТЕСТЕРА РОУТЕРА ================")
        print("1. Перевірити чи роутер увімкнений")
        print("2. Увімкнути або вимкнути роутер")
        print("3. Перевірити підключення до інтернету")
        print("4. Перевірити кількість підключених пристроїв")
        print("5. Змінити пароль Wi-Fi мережі")
        print("6. Переглянути поточний стан роутера")
        print("7. АВТОТЕСТ (просунутий режим)")
        print("0. Вихід")
        print("=======================================================")

        choice = read_menu_choice()

        if choice == 1:
            # Перевірка стану живлення
            print("\n[Перевірка]")
            if router.is_router_on():
                print("Роутер: УВІМКНЕНО.")
            else:
                print("Роутер: ВИМКНЕНО.")

        elif choice == 2:
            # Увімкнути або вимкнути
            print("\n[Зміна стану живлення]")
            print("1 — Увімкнути")
            print("2 — Вимкнути")
            sub = read_menu_choice()
            if sub == 1:
                router.turn_on()
                print("Готово: роутер увімкнено.")
            elif sub == 2:
                router.turn_off()
                print("Готово: роутер вимкнено (інтернет відключено).")
            else:
                print("Помилка: невірний підпункт.")

        elif choice == 3:
            # Перевірка підключення до інтернету (з можливістю змінити стан)
            print("\n[Перевірка підключення до інтернету]")
            if router.internet_status():
                print("Інтернет: Є підключення.")
            else:
                print("Інтернет: Немає підключення.")
            # Додатково: запропонувати змінити стан (відповідає техвимозі «реалізувати методи зміни стану»)
            if read_yes_no("Бажаєте змінити стан інтернету? (т/н): "):
                desired = read_yes_no("Увімкнути інтернет? (т/н): ")
                ok = router.set_internet_state(desired)
                if ok:
                    print("Стан інтернету змінено.")
                else:
                    print("Не вдалося змінити: спочатку увімкніть роутер (пункт 2).")

        elif choice == 4:
            # Перевірка кількості підключених пристроїв
            print("\n[Перевірка пристроїв]")
            count = router.connected_devices()
            print(f"Підключені пристрої: {count}")
           

        elif choice == 5:
            # Зміна пароля Wi-Fi з перевіркою довжини
            print("\n[Зміна пароля Wi-Fi]")
            new_pass = input("Введіть новий пароль (мінімум 8 символів): ").strip()
            ok = router.change_wifi_password(new_pass)
            if ok:
                print("Пароль успішно змінено.")
            else:
                print("Помилка: пароль занадто короткий (менше 8 символів).")

        elif choice == 6:
            # Повний звіт про стан роутера
            print("\n" + router.status_report())

        elif choice == 7:
            # Режим автоматичного тестування
            print("\n" + router.auto_test())

        elif choice == 0:
            # Вихід із програми
            print("\nВихід. Дякую за використання тестера роутера!")
            break

        else:
            # Обробка неправильного вибору меню
            print("\nПомилка: такого пункту меню не існує. Спробуйте ще раз.")


# Точка входу
if __name__ == "__main__":
    main()
