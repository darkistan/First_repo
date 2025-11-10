# Користувач вводить температуру і час доби
temp = float(input("Введіть температуру в кімнаті: "))
time_of_day = input("Введіть час доби (morning, day, evening, night): ")

# Перевірка умов і виведення рішення
if temp < 18:
    action = "увімкнути обігрів"
elif 18 <= temp <= 24:
    action = "нічого не змінювати"
else:
    action = "увімкнути охолодження"

# Винятки
if time_of_day == "night" and temp < 16:
    action = "обігрів увімкнено на максимум"
elif time_of_day == "day" and temp > 27:
    action = "охолодження увімкнено на максимум"

print("Рішення термостата:", action)
