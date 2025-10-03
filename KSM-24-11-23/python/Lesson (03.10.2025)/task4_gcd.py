# Задача 4:
# Знайти НСД (найбільший спільний дільник) двох цілих чисел.


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        raise ValueError('НСД невизначений для 0 і 0')
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    pairs = [(48, 18), (0, 5), (270, 192), (-24, 36)]
    for a, b in pairs:
        print(f'НСД({a}, {b}) = {gcd(a, b)}')
