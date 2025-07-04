# Внешние библиотеки
# Графика
# PIL - Python Image Library
# RGB
# thumbnail
from PIL import Image, ImageDraw

RED = (255, 0, 0)
WHITE = (255, 255, 255)
POLY = [(50, 50), (150,50), (150,150)]

image = Image.new('RGB', (600, 400), (0, 0, 255))
image.save('./images/blue.jpg')

draw = ImageDraw.Draw(image)
draw.line((0, 0, 600, 400),fill=RED, width=5)
draw.line((600, 0, 0, 400),fill=RED, width=5)
draw.rectangle((10, 10, 590, 390), outline=WHITE)
draw.ellipse((250, 150, 350, 250), fill=WHITE)

draw.polygon(POLY, outline='green', width=5)
draw.text((150, 50), 'Текст', fill=WHITE, font_size=45)

image.save('./images/blue.jpg')