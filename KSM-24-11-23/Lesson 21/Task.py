login = input("Введіть логін: ")
password = input("Введіть пароль: ")

# Перевірка на правильність введених даних
if login == "admin" and password == "111222":
    print("Ви увійшли в систему")
elif login != "admin":
    print("Невірний логін")
elif password != "111222":
    print("Невірний пароль")