def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    val = input("Введіть число: ")
    if not val.isdigit():
        print("Невірне число!")
        continue

    number = int(val)
    if is_prime(number):
        print(f"Число {number} є простим.")
    else:
        print(f"Число {number} не є простим.")
    break
