from datetime import date, datetime
import calendar
from typing import Optional

class DeviceService:
    # Рівень 1
    def DiagnoseDevice(self, deviceType: str) -> str:
        d = deviceType.strip().lower()
        if "комп" in d:
            return "Комп'ютер: перевірка ОЗП пройдена"
        if "смартфон" in d or "телефон" in d:
            return "Смартфон: батарея розряджається швидко"
        if "праль" in d:
            return "Пральна машина: потрібна перевірка помпи"
        return f"{deviceType}: базова діагностика завершена"

    def CheckBatteryLevel(self, batteryPercentage: int) -> str:
        p = max(0, min(100, batteryPercentage))
        if p >= 75:
            return "Високий"
        if p >= 30:
            return "Середній"
        return "Низький"

    def IsDeviceOperational(self, powerOn: bool, errorFlag: bool) -> bool:
        return bool(powerOn) and not bool(errorFlag)

    # Рівень 2
    def RepairDevice(self, deviceType: str, hasSpareParts: bool) -> str:
        # локальні методи
        def assess_complexity(dt: str) -> int:
            dt = dt.lower()
            if "праль" in dt: return 3
            if "смартфон" in dt or "комп" in dt: return 2
            return 1

        def estimate_time_minutes(complexity: int, parts: bool) -> int:
            base = {1: 30, 2: 90, 3: 180}
            t = base.get(complexity, 60)
            if not parts:
                t += 120
            return t

        c = assess_complexity(deviceType)
        t = estimate_time_minutes(c, hasSpareParts)
        if hasSpareParts:
            return f"Ремонт успішний (складність {c}, ≈{t} хв)"
        return f"Потрібні додаткові деталі (складність {c}, ≈{t} хв)"

    def OptimizePerformance(self, currentLoad: int, maxLoad: int) -> bool:
        if maxLoad <= 0:
            return False
        ratio = currentLoad / maxLoad
        if ratio <= 0.8:
            return True
        return (currentLoad * 0.75) / maxLoad <= 0.8

    def ScheduleMaintenance(self, deviceType: str, lastMaintenanceDate: date) -> date:
        def add_months(d: date, months: int) -> date:
            month = d.month - 1 + months
            year = d.year + month // 12
            month = month % 12 + 1
            day = min(d.day, calendar.monthrange(year, month)[1])
            return date(year, month, day)
        return add_months(lastMaintenanceDate, 6)

    # Рівень 3
    def PrintDeviceReport(self, deviceType: str, batteryLevel: int, isOperational: bool,
                          lastMaintenanceDate: Optional[date] = None,
                          currentLoad: Optional[int] = None, maxLoad: Optional[int] = None) -> None:
        diag = self.DiagnoseDevice(deviceType)
        batt = self.CheckBatteryLevel(batteryLevel)
        op = "працює коректно" if isOperational else "не працює коректно"
        print("\nЗВІТ")
        print("------")
        print(f"{deviceType}: {op}")
        print(f"Діагностика: {diag}")
        print(f"Рівень батареї: {batteryLevel}% ({batt})")
        if lastMaintenanceDate:
            next_maint = self.ScheduleMaintenance(deviceType, lastMaintenanceDate)
            print(f"Останнє обслуговування: {lastMaintenanceDate.isoformat()}")
            print(f"Наступне обслуговування: {next_maint.isoformat()}")
        if currentLoad is not None and maxLoad is not None:
            ok = self.OptimizePerformance(currentLoad, maxLoad)
            print("Оптимізація продуктивності пройшла успішно" if ok else "Оптимізація не допомогла — навантаження надто велике")
        print("------")

    # "Перевантаження"
    def RepairDevice_no_params(self) -> str:
        return "Ремонт виконано зі спеціальним інструментом. Ремонт успішний"

# використання з вводом від користувача
def parse_bool(s: str) -> bool:
    return s.strip().lower() in {"1","true","так","y","yes","t"}

if __name__ == "__main__":
    svc = DeviceService()

    device = input("Введіть тип техніки (наприклад: комп'ютер, смартфон, пральна машина): ").strip()
    battery_input = input("Введіть рівень батареї 0-100: ").strip()
    try:
        battery = int(battery_input)
    except ValueError:
        battery = 0

    power_on = parse_bool(input("Пристрій увімкнений? (true/false або так/ні): "))
    error_flag = parse_bool(input("Чи є помилки? (true/false або так/ні): "))

    last_maint_input = input("Останнє обслуговування (YYYY-MM-DD) або пусто: ").strip()
    last_maint_date = None
    if last_maint_input:
        try:
            last_maint_date = datetime.strptime(last_maint_input, "%Y-%m-%d").date()
        except ValueError:
            print("Невірний формат дати — пропущено інформацію про останнє обслуговування.")

    # навантаження для оптимізації
    current_load = None
    max_load = None
    use_load = input("Ввести навантаження для оптимізації? (y/n): ").strip().lower()
    if use_load in {"y","так","yes","1"}:
        try:
            current_load = int(input("Поточне навантаження (ціле число): ").strip())
            max_load = int(input("Максимальне навантаження (ціле число): ").strip())
        except ValueError:
            print("Невірний ввід навантаження — пропущено оптимізацію.")
            current_load = None
            max_load = None

    # Вивід звіту
    is_op = svc.IsDeviceOperational(power_on, error_flag)
    svc.PrintDeviceReport(device, battery, is_op, last_maint_date, current_load, max_load)

    # Рішення про ремонт
    diag = svc.DiagnoseDevice(device)
    need_repair = (not is_op) or ("потріб" in diag.lower()) or ("батарея" in diag.lower())
    if not need_repair:
        print("Ремонт не потрібен")
    else:
        has_parts = parse_bool(input("Чи є запчастини для ремонту? (true/false або так/ні): "))
        print(svc.RepairDevice(device, has_parts))

    # Перевантажений варіант ремонту
    tool_repair = parse_bool(input("Спробувати ремонт зі спеціальним інструментом? (true/false або так/ні): "))
    if tool_repair:
        print(svc.RepairDevice_no_params())
