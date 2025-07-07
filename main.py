from PIL import Image  # Ctrl + Alt + O = убрать неиспользуемые методы

orig = Image.open('./images/sunny_day_2.jpg').convert('RGB')

up = orig.crop((0, 0, 600, 200))  # половина изображения - верхняя часть
down = orig.crop((0, 200, 600, 400))  # половина изображения - нижняя часть

new = Image.new('RGB', (600, 400))

new.paste(down, (0, 0))  # верхний левый угол по этим координатам
new.paste(up, (0, 200))  # верхний левый угол по этим координатам

new.show()

from PIL import ImageFilter, ImageEnhance

orig = Image.open('./images/rabbit.jpg').convert('RGB')
# Размытие
blur_image = orig.filter(ImageFilter.GaussianBlur(1))
blur_image.show()
# Усиление резкости
enchancer = ImageEnhance.Sharpness(orig)
sharpened_image = enchancer.enhance(4.0)
sharpened_image.show()
# получить контуры изображения
edges = orig.filter(ImageFilter.FIND_EDGES)
edges.show()
