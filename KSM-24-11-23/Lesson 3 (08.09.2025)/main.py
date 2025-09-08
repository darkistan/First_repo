
MIN_PER_HOUR = 60
MINUTES_PER_DAY = 24 * MIN_PER_HOUR


print("Вкажи дані у простому форматі. Якщо помилка формату — програма завершить роботу.")

# Тип дня: 1 - робочий (навчання = 6), 2 - вихідний
typ = input("Тип дня (1 — робочий, 2 — вихідний) >>> ").strip()
if typ not in ("1", "2"):
    print("Невірний тип дня. Очікував 1 або 2. Вихід.")
    raise SystemExit

# Час пробудження
wake_s = input("О котрій прокидаєшся? (HH:MM) >>> ").strip()
try:
    p = wake_s.split(':')
    wake_h = int(p[0]); wake_m = int(p[1])
    wake_min = wake_h * MIN_PER_HOUR + wake_m
except:
    print("Невірний формат часу пробудження. Вихід.")
    raise SystemExit

# Час сну
sleep_s = input("О котрій лягаєш спати? (HH:MM) >>> ").strip()
try:
    p = sleep_s.split(':')
    sleep_h = int(p[0]); sleep_m = int(p[1])
    sleep_min = sleep_h * MIN_PER_HOUR + sleep_m
except:
    print("Невірний формат часу сну. Вихід.")
    raise SystemExit

# Години (допускаємо крапку або кому)
def_to_float = False
if typ == "1":
    learn_h = 6.0
    print("Робочий день: навчання = 6.0 год.")
    s = input("Скільки годин відпочинку? >>> ").strip().replace(',', '.')
    try:
        rest_h = float(s)
    except:
        print("Невірний ввід для відпочинку. Вихід.")
        raise SystemExit
    s = input("Скільки годин хобі? >>> ").strip().replace(',', '.')
    try:
        hobby_h = float(s)
    except:
        print("Невірний ввід для хобі. Вихід.")
        raise SystemExit
else:
    s = input("Скільки годин навчанню? >>> ").strip().replace(',', '.')
    try:
        learn_h = float(s)
    except:
        print("Невірний ввід для навчання. Вихід.")
        raise SystemExit
    s = input("Скільки годин відпочинку? >>> ").strip().replace(',', '.')
    try:
        rest_h = float(s)
    except:
        print("Невірний ввід для відпочинку. Вихід.")
        raise SystemExit
    s = input("Скільки годин хобі? >>> ").strip().replace(',', '.')
    try:
        hobby_h = float(s)
    except:
        print("Невірний ввід для хобі. Вихід.")
        raise SystemExit

# Просте обмеження
if learn_h < 0 or rest_h < 0 or hobby_h < 0:
    print("Час не може бути від'ємним. Вихід.")
    raise SystemExit

# Доступний час між пробудженням і сном (в хвилинах)
if sleep_min <= wake_min:
    available = (sleep_min + MINUTES_PER_DAY) - wake_min
else:
    available = sleep_min - wake_min

# Запитуваний час в хвилинах
requested = int(round((learn_h + rest_h + hobby_h) * MIN_PER_HOUR))

print("\n--- Аналіз ---")
print(f"Доступно: {available / MIN_PER_HOUR:.2f} год.  Заплановано: {requested / MIN_PER_HOUR:.2f} год.")

if requested > available:
    deficit = requested - available
    print(f"\nЧасу не вистачає: потрібно ще {deficit / MIN_PER_HOUR:.2f} год.")
    # Проста порада: скоротити хобі, потім відпочинок, потім навчання
    need = deficit
    # спробуємо скоротити хобі
    hobby_min = int(round(hobby_h * MIN_PER_HOUR))
    cut_hobby = hobby_min if hobby_min < need else need
    if cut_hobby > 0:
        print(f"Пропозиція: скоротити хобі на {cut_hobby / MIN_PER_HOUR:.2f} год.")
        need -= cut_hobby
    # потім відпочинок
    rest_min = int(round(rest_h * MIN_PER_HOUR))
    cut_rest = rest_min if rest_min < need else need
    if cut_rest > 0:
        print(f"Або скоротити відпочинок на {cut_rest / MIN_PER_HOUR:.2f} год.")
        need -= cut_rest
    # потім навчання
    learn_min = int(round(learn_h * MIN_PER_HOUR))
    cut_learn = learn_min if learn_min < need else need
    if cut_learn > 0:
        print(f"Або скоротити навчання на {cut_learn / MIN_PER_HOUR:.2f} год.")
        need -= cut_learn
    if need > 0:
        print("Навіть після скорочень часу не вистачає. Можна змінити час сну або тип дня.")
else:
    leftover = available - requested
    print(f"\nУсе вміщається. Залишок вільного часу: {leftover / MIN_PER_HOUR:.2f} год.")
    # Побудова простого лінійного розкладу: навчання -> хобі -> відпочинок -> вільний час
    schedule = []
    t = wake_min
    # навчання
    dur = int(round(learn_h * MIN_PER_HOUR))
    schedule.append(("Навчання", t, t + dur))
    t = t + dur
    # хобі
    dur = int(round(hobby_h * MIN_PER_HOUR))
    schedule.append(("Хобі", t, t + dur))
    t = t + dur
    # відпочинок
    dur = int(round(rest_h * MIN_PER_HOUR))
    schedule.append(("Відпочинок", t, t + dur))
    t = t + dur
    # вільний час
    if leftover > 0:
        schedule.append(("Вільний час / підготовка до сну", t, t + leftover))
    # Функція конвертації часу 
    print("\nТвій план дня:")
    for act, start, end in schedule:
        s1 = start % MINUTES_PER_DAY
        h1 = s1 // MIN_PER_HOUR
        m1 = s1 % MIN_PER_HOUR
        s2 = end % MINUTES_PER_DAY
        h2 = s2 // MIN_PER_HOUR
        m2 = s2 % MIN_PER_HOUR
        start_str = f"{h1:02d}:{m1:02d}"
        end_str = f"{h2:02d}:{m2:02d}"
        print(f"{start_str}–{end_str} — {act}")
    print("\nГарного дня!")
