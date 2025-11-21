# Програма "GamerAssistant"

# Ввід даних від користувача
hours = int(input("Скільки годин ти грав сьогодні? "))
game = input("В яку гру ти грав сьогодні? ")

# Аналіз за кількістю годин
if 0 <= hours <= 1:
    comment_hours = "Новачок сьогодні? Поважаю силу волі!"
elif 2 <= hours <= 4:
    comment_hours = "Баланс — рівень бог. Так тримати!"
elif 5 <= hours <= 7:
    comment_hours = "Граєш серйозно. Час на перерву!"
elif hours >= 8:
    comment_hours = "Бро… можливо, час поїсти й відпочити очам?"
else:
    # На випадок від’ємних значень
    comment_hours = "Дивні години вводу, але гаразд :)"

# Аналіз за назвою гри
if game == "CS":
    comment_game = "Реакція сьогодні швидша за світло!"
elif game == "Dota":
    comment_game = "Стійкість +10. Токсичність команди −100."
elif game == "GTA":
    comment_game = "Пора з’їздити за водою, а не по Лос-Сантосу."
elif game == "Fortnite":
    comment_game = "Будуєш швидше, ніж думаєш. Це талант!"
elif game == "FIFA":
    comment_game = "Справжній чемпіон не rage-quit’ить."
else:
    comment_game = "Гра для справжніх поціновувачів! Респект."

# Порада дня
advice = "Пий воду, герой геймінгу."

# Вивід результату
print("\n=== GamerAssistant Pro Max ===")
print("Коментар за годинами:", comment_hours)
print("Коментар за грою:", comment_game)
print("Порада дня:", advice)
