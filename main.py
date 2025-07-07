from PIL import Image, ImageDraw, ImageFont

# https://fontsforyou.com/ru/specific-fonts/ttf-fonts/languageru
W = 600
H = 400

image = Image.new('RGB',
                  (W, H),
                  (0, 163, 232))

draw = ImageDraw.Draw(image)

text = 'Солнечный день'
# draw.ellipse((470, -120, 800, 120), outline='yellow', fill='yellow')
draw.circle((600, 0), 100, fill='yellow')
font = ImageFont.truetype(
    font='./fonts/main_font.ttf',  # можно использовать любой установленный шрифт
    size=40
)
# Получаем размеры текста с помощью распаковки
_, _, w, h = draw.textbbox((0, 0), text, font=font)

# Рассчитываем позицию для центрирования
x = (W - w) // 2
y = (H - h) // 2

draw.text((x, y), text, fill=(255, 255, 0), font=font)

image.save('images/sunny_day_2.jpg')  # image.show() - показать картинку без сохранения
















