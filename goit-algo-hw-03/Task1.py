from datetime import datetime

def get_days_from_today(date):
    # Перетворюємо введену дату 
    given_date = datetime.strptime(date, "%Y-%m-%d")
    
    # Отримуємо поточну дату
    today = datetime.today()
    
    # Рахуємо різницю між поточною датою та заданою
    delta = today - given_date
    
    # Повертаємо кількість днів
    return delta.days

# Приклад використання функції
print(get_days_from_today("2021-10-09"))
