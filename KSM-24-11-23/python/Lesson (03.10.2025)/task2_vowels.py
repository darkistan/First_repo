# Задача 2:
# Порахувати кількість голосних у рядку (українські та англійські голосні).


def count_vowels(s: str) -> int:
    vowels = set('aeiouyаеєиіїоуюя')
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    return count

if __name__ == '__main__':
    texts = [
        'Привіт, як справи? Hello!',
        'Звук ї в слові: їжак',
        ''
    ]
    for t in texts:
        print(f"'{t}' -> {count_vowels(t)} голосних")
