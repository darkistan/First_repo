# програма перевіряє, чи є число простим

num = int(input("Введіть ціле число: "))

# перевірка для чисел менше 2
if num < 2:
    is_prime = False
else:
    is_prime = True
    i = 2
    # перевірка дільників
    while i * i <= num:
        
        if num % i == 0:
            is_prime = False
            break
        i += 1

# вивід результату
if is_prime:
    print("Число є простим")
else:
    print("Число не є простим")
