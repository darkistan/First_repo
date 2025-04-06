import math

# Значення катетів
a = 18
b = 6 * math.sqrt(3)

# Знаходимо перший кут (в радіанах)
angle1_rad = math.atan(a / b)

# Перетворюємо радіани в градуси
angle1_deg = math.degrees(angle1_rad)

# Другий кут - це 90 градусів мінус перший кут
angle2_deg = 90 - angle1_deg

# Виводимо кути
print(f"Перший кут: {angle1_deg:.2f} градусів")
print(f"Другий кут: {angle2_deg:.2f} градусів")
