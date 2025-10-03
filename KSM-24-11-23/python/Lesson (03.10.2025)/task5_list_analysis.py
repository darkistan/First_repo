# Задача 5:
# Дано список чисел. Порахувати: кількість парних, кількість непарних (рахувати тільки цілі),
# і середнє арифметичне всіх елементів.


from typing import List, Tuple, Optional

def analyze_list(nums: List[float]) -> Tuple[int, int, Optional[float]]:
    even = 0
    odd = 0
    for x in nums:
        # Рахуємо парні/непарні тільки якщо це ціле число
        if isinstance(x, int) or (isinstance(x, float) and x.is_integer()):
            if int(x) % 2 == 0:
                even += 1
            else:
                odd += 1
    avg = None
    if len(nums) > 0:
        avg = sum(nums) / len(nums)
    return even, odd, avg

if __name__ == '__main__':
    examples = [
        [1,2,3,4,5,6],
        [2.0, 3.0, 4.5, 7],
        []
    ]
    for ex in examples:
        e,o,avg = analyze_list(ex)
        print(f'{ex} -> парних: {e}, непарних: {o}, середнє: {avg}')
