# Запит даних у користувача
login = input("Введіть логін: ")
password = input("Введіть пароль: ")
secret_code = input("Введіть секретний код: ")

# Правильні значення 
right_login = "admin"
right_password = "qwerty"
right_code1 = "1111"
right_code2 = "2222"

# Перевірка з використанням логічних операторів and, or
is_valid = (login == right_login) and (password == right_password) and ((secret_code == right_code1) or (secret_code == right_code2))

# Вивід результату. Використання not для заперечення умови.
if is_valid:
    print("Доступ дозволено")
if not is_valid:
    print("Доступ заборонено")
