from PIL import Image, ImageDraw
# объявляем константы цветов
BLUE = (125, 190, 255)
YELLOW = (255, 242, 0)
# создаём холст
image = Image.new('RGB', (600, 400), BLUE)

draw = ImageDraw.Draw(image)
# рисуем солнце и пишем заголовок
draw.ellipse((500, -100, 700, 100), fill=YELLOW)
draw.text((170, 160), 'SUNNY DAY', fill=YELLOW, font_size=45)
# сохраняем изображение
image.save('./images/sunny_day.jpg')