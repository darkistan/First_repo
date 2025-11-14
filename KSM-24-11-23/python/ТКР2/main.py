import random

# комп'ютер загадує число
secret_num = random.randint(1, 50)

# кількість спроб
tries = 7

# цикл спроб
while tries > 0:
    user_num = int(input("Введіть число від 1 до 50: "))

    if user_num == secret_num:
        print("Ви вгадали!")
        break
    else:
        tries -= 1  # зменшуємо кількість спроб

        if user_num < secret_num:
            print("Більше")
        else:
            print("Менше")

        print("Залишилось спроб:", tries)

# якщо спроб не лишилось
if tries == 0:
    print("Гру завершено. Було загадано число", secret_num)
