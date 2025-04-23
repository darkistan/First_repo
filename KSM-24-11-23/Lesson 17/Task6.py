login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login != "admin":
    print("Неправильний логін")
else:
    if password != "admin111222":
        print("Неправильний пароль")
    else:
        print("Ви зайшли в свій аккаунт")
