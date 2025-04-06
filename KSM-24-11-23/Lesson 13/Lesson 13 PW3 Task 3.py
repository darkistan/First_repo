viruses = 2
print("Задача 3: Кількість вірусів по днях:")
for day in range(1, 7):
    viruses *= 2
    print(f"  День {day}: {viruses} вірусів")