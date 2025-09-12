# office_booking_minimal.py
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple, Optional

@dataclass
class Employee:
    id: int
    name: str
    department: str
    email: str

@dataclass
class Seat:
    seat_id: str
    floor: int
    monitor: bool
    laptop: bool
    dock: bool
    conditioner: bool

@dataclass
class Booking:
    employee_id: int
    seat_id: str
    when: datetime  # точна дата та час бронювання

class BookingSystem:
    def __init__(self):
        self._employees: Dict[int, Employee] = {}
        self._seats: Dict[str, Seat] = {}
        self._bookings: List[Booking] = []
        self._next_emp_id = 1

    # 1. Додати співробітника
    def add_employee(self, name: str, department: str, email: str) -> Employee:
        emp = Employee(self._next_emp_id, name.strip(), department.strip(), email.strip())
        self._employees[self._next_emp_id] = emp
        self._next_emp_id += 1
        return emp

    # 2. Додати місце
    def add_seat(self, seat_id: str, floor: int,
                 monitor: bool, laptop: bool, dock: bool, conditioner: bool) -> Seat:
        sid = seat_id.strip()
        if sid in self._seats:
            raise ValueError("ID місця вже існує")
        seat = Seat(sid, floor, monitor, laptop, dock, conditioner)
        self._seats[sid] = seat
        return seat

    # 3. Робити бронювання на вказану дату й час
    def create_booking(self, employee_id: int, seat_id: str, when: datetime) -> None:
        if employee_id not in self._employees:
            raise ValueError("Невідомий співробітник")
        if seat_id not in self._seats:
            raise ValueError("Невідоме місце")
        # строгий тест: не дозволяємо бронювання, якщо вже є бронювання
        for b in self._bookings:
            if b.seat_id == seat_id and b.when == when:
                raise ValueError("Місце вже заброньоване в цей час")
        self._bookings.append(Booking(employee_id, seat_id, when))

    # 4. Перевіряти доступність місця чи воно не заброньоване іншим
    def is_seat_available(self, seat_id: str, when: datetime) -> bool:
        if seat_id not in self._seats:
            raise ValueError("Невідоме місце")
        for b in self._bookings:
            if b.seat_id == seat_id and b.when == when:
                return False
        return True

    # 5.a Топ-3 найпопулярніші місця (за кількістю бронювань)
    def top3_seats(self) -> List[Tuple[str, int]]:
        counts: Dict[str, int] = {}
        for b in self._bookings:
            counts[b.seat_id] = counts.get(b.seat_id, 0) + 1
        items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return items[:3]

    # 5.b Кількість бронювань у кожному відділі
    def bookings_per_department(self) -> Dict[str, int]:
        dept_counts: Dict[str, int] = {}
        for b in self._bookings:
            emp = self._employees.get(b.employee_id)
            if emp:
                dept = emp.department
                dept_counts[dept] = dept_counts.get(dept, 0) + 1
        return dept_counts

    # 5.c Співробітник який найчастіше бронює
    def top_employee(self) -> Optional[Tuple[Employee, int]]:
        emp_counts: Dict[int, int] = {}
        for b in self._bookings:
            emp_counts[b.employee_id] = emp_counts.get(b.employee_id, 0) + 1
        if not emp_counts:
            return None
        top_id = max(emp_counts.items(), key=lambda x: x[1])[0]
        return (self._employees[top_id], emp_counts[top_id])

# ---------- Меню ----------
def parse_bool(s: str) -> bool:
    return s.strip().lower() in ("true", "так", "y", "1", "yes")

def input_datetime(prompt_date: str, prompt_time: str) -> datetime:
    while True:
        d = input(prompt_date).strip()
        t = input(prompt_time).strip()
        try:
            return datetime.strptime(f"{d} {t}", "%Y-%m-%d %H:%M")
        except Exception:
            print("Невірний формат. Дата YYYY-MM-DD, час HH:MM (24h). Спробуйте ще раз.")

def main():
    system = BookingSystem()
    while True:
        print("\nМеню програми")
        print("1 Додати співробітника")
        print("2 Додати місце")
        print("3 Забронювати місце")
        print("4 Перевірити доступність")
        print("5 Показати статистику")
        print("6 Вихід")
        choice = input("Вибір: ").strip()
        if choice == "1":
            name = input("Ім'я: ").strip()
            dept = input("Відділ: ").strip()
            email = input("Email: ").strip()
            emp = system.add_employee(name, dept, email)
            print(f"Додано співробітника. ID = {emp.id}")
        elif choice == "2":
            sid = input("ID місця: ").strip()
            floor_str = input("Поверх (число): ").strip()
            floor = int(floor_str)
            monitor = parse_bool(input("Монітор (true/false): "))
            laptop = parse_bool(input("Ноутбук (true/false): "))
            dock = parse_bool(input("Док (true/false): "))
            conditioner = parse_bool(input("Кондиціонер (true/false): "))
            try:
                system.add_seat(sid, floor, monitor, laptop, dock, conditioner)
                print("Місце додано.")
            except ValueError as e:
                print("Помилка:", e)
        elif choice == "3":
            emp_id = int(input("ID співробітника: ").strip())
            seat_id = input("ID місця: ").strip()
            when = input_datetime("Дата (YYYY-MM-DD): ", "Час (HH:MM): ")
            try:
                system.create_booking(emp_id, seat_id, when)
                print("Бронювання зроблено.")
            except ValueError as e:
                print("Помилка:", e)
        elif choice == "4":
            seat_id = input("ID місця: ").strip()
            when = input_datetime("Дата (YYYY-MM-DD): ", "Час (HH:MM): ")
            try:
                available = system.is_seat_available(seat_id, when)
                print("Доступне." if available else "Зайняте.")
            except ValueError as e:
                print("Помилка:", e)
        elif choice == "5":
            print("\nСтатистика:")
            top3 = system.top3_seats()
            if top3:
                print("Топ-3 місць (ID: кількість):")
                for sid, cnt in top3:
                    print(f"{sid}: {cnt}")
            else:
                print("Топ-3 місць: немає бронювань.")
            dept = system.bookings_per_department()
            if dept:
                print("\nБронювання по відділах:")
                for dname, cnt in dept.items():
                    print(f"{dname}: {cnt}")
            else:
                print("\nБронювання по відділах: немає бронювань.")
            top_emp = system.top_employee()
            if top_emp:
                emp, cnt = top_emp
                print(f"\nСпівробітник, що найчастіше бронює: {emp.name} (ID={emp.id}) — {cnt} раз(и)")
            else:
                print("\nНемає даних про співробітників, що бронюють.")
        elif choice == "6":
            break
        else:
            print("Невірний вибір. Введіть 1-6.")

if __name__ == "__main__":
    main()
