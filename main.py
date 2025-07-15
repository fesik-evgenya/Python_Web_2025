# # Погода через API
# import requests
# from PIL import Image
# import io
#
# API_KEY = 'c747bf84924be997ff13ac5034fa3f86'
# URL = 'http://api.openweathermap.org/data/2.5/weather'
# CITY = 'Санкт-Петербург'
#
# params = {
#     'q': CITY,
#     'appid': API_KEY,
#     'units': 'metric',
#     'lang': 'ru'
# }
#
# response = requests.get(URL, params=params)
# result = response.json()
# # print(result)
#
# weather = result['weather'][0]['description']
# temperature = result['main']['temp']
# humidity = result['main']['humidity']
# wind = result['wind']['speed']
# data = result['coord']
# ll = f'{data['lon']},{data['lat']}'
# # print(ll)
#
#
# print(f'Сегодня в городе {CITY}: {weather}')
# print(f'Температура: {temperature:.1f}\xB0C')
# print(f'Влажность: {humidity}%')
# print(f'Скорость ветра: {wind} м/с')
# link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
# image = requests.get(link).content
# if image:
#     im = Image.open(io.BytesIO(image)).convert('RGB')
#     im.save('map.jpg')
#
# # Декораторы
# def answer(question):
#     return ('думайте сами')
#
#
# def dialog():
#     def answer(question):
#         if question.lower().startswith('когда'):
#             return 'Никогда'
#         else:
#             return 'Упппс'
#     question = input()
#     while question != '':
#         print(answer(question))
#         question = input()
#
# dialog()
#
# # меняем функционал одной функции с помощью другой функции - декоратор
# def upper_case_print(old_func):
#     def new_func(*args, **kwargs):
#         case = kwargs.pop('case', None)
#         if case == 'U':
#             args = [str(arg).upper() for arg in args]
#         elif case == 'L':
#             args = [str(arg).lower() for arg in args]
#         old_func(*args, **kwargs)
#     return new_func
#
# new_print = upper_case_print(print)
# new_print('Привет, Пока')
# new_print('Привет, Пока', case='U')
# new_print('Привет, Пока', case='L')
#
# def outer():
#     x = 5
#
#     def inner():
#         nonlocal x
#         print('Nonlocal x=', x)
#         x = 10
#     inner()
#     print('New x=', x)
#
# outer()
#
# def logger(func):
#     counter = 0
#     def decorated_func(*args, **kwargs):
#         nonlocal counter
#         counter += 1
#         print(counter, '->', 'Аргументы', args, 'Именованные аргументы:', kwargs)
#         result = func(*args, **kwargs)
#         print('_____', 'Результат:', result)
#         return result
#     return decorated_func
#
# @logger
# def make_burger(meal='говядиной', onion=False, tomato=False):
#     print('Булочка')
#     if onion:
#         print('Луковые кольца')
#     print('Котлета с', meal)
#     if tomato:
#         print('Помидоры')
#     print('Булочка')
#
# make_burger(meal='Бараниной',onion=True)

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'Функция исполнялась: {finish - start:.4f} сек.')
        return result
    return wrapper

@timeit
def test():
    time.sleep(0.8)


test()