base = int(input("Введіть число: "))
power = int(input("Введіть степінь: "))
result = 1
for i in range(power):
    result *= base
print(f"{base} в степені {power} = {result}")
