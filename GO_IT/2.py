import random

def get_numbers_ticket(min, max, quantity):
    # Генеруємо унікальний список випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    return numbers

# Приклад використання функції
print(get_numbers_ticket(1, 49, 6))
