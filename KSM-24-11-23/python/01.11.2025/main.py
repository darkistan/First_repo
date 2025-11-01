# Генерація зображення зі знайденими словами

import re  
from PIL import Image, ImageDraw, ImageFont  # для створення PNG-зображення

# Зчитування тексту з рядка 
text = input("Введіть текст: ")

# Пошук усіх слів, що починаються з великої літери 
pattern = r"\b[А-ЯA-ZЇІЄҐ][а-яa-zїієґА-ЯA-Z]*\b"
words = re.findall(pattern, text)

# Створення зображення PNG з “хмарою слів”
# Параметри зображення
img_width = 1000
img_height = 700
bg_color = "white"
text_color = "black"

# Створюємо полотно
image = Image.new("RGB", (img_width, img_height), bg_color)
draw = ImageDraw.Draw(image)

# Шрифт 
try:
    font = ImageFont.truetype("arial.ttf", 28)
except:
    font = ImageFont.load_default()

# Розміщення слів простими рядками з перенесенням
x = 30
y = 30
line_spacing = 12  # додатковий інтервал між рядками
space_w = draw.textlength(" ", font=font)

for w in words:
    word_w = draw.textlength(w, font=font)
    # якщо слово не вміщується в рядок — переносимо на новий рядок
    if x + word_w >= img_width - 30:
        x = 30
        # висоту беремо за метрикою шрифту
        ascent, descent = font.getmetrics()
        y += ascent + descent + line_spacing

    # якщо не вистачає місця по висоті — завершуємо
    if y >= img_height - 40:
        break

    # малюємо слово
    draw.text((x, y), w, fill=text_color, font=font)

    # додаємо пробіл після слова
    x += word_w + space_w

# Збереження PNG
image.save("word_cloud.png")
print("Зображення збережено як word_cloud.png")
