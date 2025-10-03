# Задача 10:
# Згенерувати випадковий пароль заданої довжини.
# Якщо потрібні спецсимволи - включаємо їх, інакше лише букви і цифри.

import random
import string

def generate_password(length: int, special: bool = True) -> str:
    if length <= 0:
        return ''
    letters = string.ascii_letters
    digits = string.digits
    if special:
        pool = letters + digits + string.punctuation
    else:
        pool = letters + digits
    return ''.join(random.choice(pool) for _ in range(length))

if __name__ == '__main__':
    print('Декілька прикладів:')
    print(generate_password(8, True))
    print(generate_password(12, False))
    print(generate_password(14, True))
