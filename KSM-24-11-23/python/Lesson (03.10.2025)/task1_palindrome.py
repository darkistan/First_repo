# Задача 1:
# Перевірити, чи є рядок паліндромом (ігнорувати пробіли, пунктуацію і регістр).


def is_palindrome(s: str) -> bool:
    # Залишаємо тільки букви і цифри (для простоти англ. та укр. літери)
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    examples = [
        'Казак',
        'А роза упала на лапу Азора!',
        'hello',
        'Level',
    ]
    for ex in examples:
        print(f"'{ex}' -> {is_palindrome(ex)}")
