while True:
    print("\nМеню:")
    print("1 - Переміститися вверх")
    print("2 - Переміститися вправо")
    print("3 - Переміститися вниз")
    print("4 - Переміститися вліво")
    print("0 - Зупинитися")
    
    choice = input("Оберіть дію: ")

    if choice == '1':
        print("Ви перемістились вверх.")
    elif choice == '2':
        print("Ви перемістились вправо.")
    elif choice == '3':
        print("Ви перемістились вниз.")
    elif choice == '4':
        print("Ви перемістились вліво.")
    elif choice == '0':
        print("Зупинка.")
        break
    else:
        print("Невідома команда.")
