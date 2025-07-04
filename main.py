# Встроенные библиотеки - модули
# библиотека - это сборник подпрограмм, которые можно включить в другую программу
# PyPI - Python Package Index (pypi.org) - хранилище библиотек Python

lst = [1, 5, 2, 3, 5]
min_value = min(lst)  # минимальное значение последовательности
max_value = max(lst)  # максимальное значение последовательности

print(min_value, max_value)

# import math as m
# from math import *

from math import pi, sqrt, sin, radians, hypot

# print dir(m)
# print(dir(m)

print('Число Пи: ', pi)
print('Квадратный корень 4: ', sqrt(4))
print('Синус 30°: ', round(sin(radians(30))), 2)
print('Гипотенуза для 3 и 2: ', hypot(3, 2))

import random as r

for _ in range(10):
    # print(r.randint(0, 10))  # рандомное число от 0 до 10 включительно
    print(r.randrange(0, 10, 2))  # рандомное чётное число от 0 до 10

lst = list(range(0, 10))

res = r.choice(lst)  # работает со всеми итерируемыми объектами кроме словаря и множества
print(res)

print(r.choice(['орёл', 'решка']))  # подкидывание монетки

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    }

keys = list(d.keys())
key = r.choice(keys)

print(d[key])

zara = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685', '\u2686',]

for _ in range(10):
    print(r.choice(zara), r.choice(zara))

# чем отличается choice от sample
# при многократном выборе choice может повторять выбор, а sample не повторяет
for _ in range(10):
    print(r.sample(zara, k=2))

# генерация случайного пароля - 8 символов ( 1 большая буква, 1 символ, 1 цифра)
N = 8

abc = list('abcdefghijklmnopqrstuvwxyz')
num = list('1234567890')
spec = list('@#$&')

r.shuffle(abc)
r.shuffle(num)
r.shuffle(spec)


temp = abc[:N - 3]
temp.append(r.choice(abc).upper())
temp.append(r.choice(num))
temp.append(r.choice(spec))
r.shuffle(temp)
res = ''.join(temp)

print(res)

странный seed
r.seed(5)
print(r.random())

модуль DateTime = с системных часов компьютера (на котором запускается)

import datetime as dt

print(dt.datetime.now())
print(dt.datetime.now().date())  # вытащили дату
print(dt.datetime.now().time())  # вытащили время

# вытащить день, месяц(m), год(y - кратко + Y - полный)
print('Сегодня', dt.datetime.now().strftime('%d'), 'день')
print('Сегодня', dt.datetime.now().strftime('%m'), 'месяц')
print('Сегодня', dt.datetime.now().strftime('%Y'), 'год')

print('Время:', dt.datetime.now().strftime('%H:%M:%S'))  # часы:минуты:секунды

my_time = dt.time(15, 27, 32)
print(my_time)

my_date = dt.date(2025, 7, 4)
print(my_date)

my_date_time = dt.datetime.combine(my_date, my_time)
print(my_date_time)

date1 = dt.date(2025, 6, 15)
date2 = dt.date(2025, 7,3)
delta = date2 - date1
print(delta)

from pprint import pprint

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

pprint(matrix)