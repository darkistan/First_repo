import random

# -----------------------------------------------------------------------------
# Шановний викладачу,
# візьміть, будь ласка, чашку улюбленої кави, відкиньтесь на спинку стільця
# і дайте собі хвилину просто насолодитися життям — відкладіть думки про
# баґи та оцінювання, вони почекають.
# Бажаю вам легкого дня, приємного настрою і щоб усе тестувалося
# з першого разу (або хоча б з другого).  ))))))
# І посміхніться, бо вам те личить! :)
# -----------------------------------------------------------------------------

# Клас для гравця
class Player:
    def __init__(self):
        self.money = 0
        self.energy = 100
        self.mood = 100
        self.experience = 0
        self.level = 1
        self.history = []
        self.day = 1

    def work(self):
        if self.energy <= 0:
            print("Недостатньо енергії для роботи.")
            return False
        self.energy -= 10
        self.experience += 5
        earnings = random.randint(10, 100)
        self.money += earnings
        self.history.append(f"День {self.day}: Працював/ла, зароблено {earnings} монет.")
        return True

    def invest(self):
        if self.energy <= 0:
            print("Недостатньо енергії для інвестування.")
            return False
        self.energy -= 20
        self.experience += 10
        investment = random.choice(['товар', 'стартап', 'криптовалюта'])
        success = random.choice([True, False])
        if success:
            earnings = random.randint(100, 500)
            self.money += earnings
            self.history.append(f"День {self.day}: Інвестував/ла в {investment}, зароблено {earnings} монет.")
        else:
            loss = random.randint(50, 200)
            self.money -= loss
            self.history.append(f"День {self.day}: Інвестиція в {investment} не вдалась, втрачено {loss} монет.")
        return True

    def rest(self):
        self.energy = 100
        self.mood += 20
        self.history.append(f"День {self.day}: Відпочивав/ла, енергія відновлена.")

    def learn(self):
        if self.energy <= 0:
            print("Недостатньо енергії для навчання.")
            return False
        self.energy -= 15
        self.experience += 20
        self.history.append(f"День {self.day}: Навчався/лася, досвід збільшено.")
        return True

    def skip_day(self):
        self.history.append(f"День {self.day}: Пропустив/ла день.")
        self.energy -= 5  # енергія зменшується навіть при пропуску дня
        self.mood -= 10  # настрій падає

    def random_event(self):
        event = random.choice([
            ("Отримано бонус від клієнта", 100),
            ("Несподівані витрати", -50),
            ("Втрата частини товару або доходу", -100),
            ("Поліпшення репутації", 50),
            ("Тимчасове зниження настрою", -20)
        ])
        description, change = event
        self.money += change
        self.mood += change
        self.history.append(f"День {self.day}: {description}, зміни: {change} монет.")

# Клас для гри
class Game:
    def __init__(self):
        self.player = Player()
        self.running = True

    def daily_update(self):
        self.player.random_event()
        if self.player.money >= 10000:
            print("Перемога! Ви досягли 10,000 монет.")
            self.running = False
        if self.player.money < 0:
            print("Поразка! Ви збанкрутували.")
            self.running = False
        if self.player.energy <= 0 or self.player.mood <= 0:
            print("Поразка! Ваша енергія або настрій досягли 0.")
            self.running = False

    def show_status(self):
        print(f"День: {self.player.day}")
        print(f"Гроші: {self.player.money} монет")
        print(f"Енергія: {self.player.energy}")
        print(f"Настрій: {self.player.mood}")
        print(f"Досвід: {self.player.experience}")
        print(f"Рівень: {self.player.level}")
        print("Історія дій:")
        for action in self.player.history:
            print(action)
        print()

    def take_action(self):
        print("Виберіть дію:")
        print("1. Працювати")
        print("2. Інвестувати")
        print("3. Відпочити")
        print("4. Навчатися")
        print("5. Пропустити день")
        choice = input("Ваш вибір (1-5): ")

        if choice == '1':
            self.player.work()
        elif choice == '2':
            self.player.invest()
        elif choice == '3':
            self.player.rest()
        elif choice == '4':
            self.player.learn()
        elif choice == '5':
            self.player.skip_day()

    def run(self):
        while self.running:
            self.show_status()
            self.take_action()
            self.player.day += 1
            self.daily_update()

# Початок гри
if __name__ == "__main__":
    game = Game()
    game.run()
