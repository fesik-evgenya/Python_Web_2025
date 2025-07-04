# Внешние библиотеки
# Графика
# PIL - Python Image Library
# RGB
# thumbnail
from PIL import Image

image = Image.open('./images/rabbit.jpg')
x, y = image.size  # распаковка
mode= image.mode
pixels = image.load()  # загрузить таблицу пикселей

print(f'Ширина = {x}, высота = {y}')
print(f'Цветовая схема: {mode}')

# # Инверсия
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # обращение идёт через кортеж
#         pixels [i, j]= b, r, g
#
# image.save('./images/rabbit2.jpg')
#
# # Негатив
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # обращение идёт через кортеж
#         pixels [i, j]= 255 - r, 255 - g, 255 - b
#
# image.save('./images/rabbit2.jpg')
#
# # Grayscale
# for i in range(x):
#     for j in range(y):
#         r, g, b = pixels[i, j]  # обращение идёт через кортеж
#         average = (r + g + b) // 3
#         pixels [i, j]= average, average, average
#
# image.save('./images/rabbit2.jpg')
#
# # Rotate
# image_rotate = image.rotate(180)
# image_rotate.save('./images/rabbit_rotate.jpg')
#
# # Отразить горизонтально
# image.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save('./images/rabbit_flip.jpg')
#
# # Вырезать нужный кусок
# # верхний левый угол = x, y; правый нижний угол = x, y
# image.crop((180, 40, 520, 430)).save('./images/rabbit_crop.jpg')
#
# # Вырезать нужный кусок
# # верхний левый угол = x, y; правый нижний угол = x, y
# x, y = image.size
# ratio = x // y
# image.resize((100, )).save('./images/rabbit_resize.jpg')