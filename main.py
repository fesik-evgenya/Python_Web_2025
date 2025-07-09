# ООП - объектно ориентированное программирование
# (encapsulation) - каждый объект это какая-то капсула.
# Применяется для безопасности.
# Класс - это прототип будущего объекта, который описывает его свойства и поведение,
# и это такой-то набор данных и методы по работе с ними.
# Экземпляр - это объект, порождённый классом
# Атрибуты - это всё что внутри класса (свойства и методы)
# Метод - это действие объекта
#
# Свойства классов:
#
# a = None
# print(a.__class__.__name__)
#
# # создали класс
# class Fruit:
#     pass
#
#
# a = Fruit() # создали экземпляр класса
#
# print(a.__class__)
#
# a.name = 'Яблоко'
# a.weight = 120
#
# print(a.name)
# print(a.weight)
#
# b = Fruit()
# b.name = 'Груша'
# b.weight = 90
#
# print(b.name, b.weight)
#
# # методы классов
# # в self - это контекстный объект,
# # в который передаётся вызванный метод ->
# # (-> это ссылка, которая ведёт на адрес в оперативной памяти)
# class Greater:
#     def hello(self, name='Noname') -> None:
#         print('Привет,', name)
#
#     def goodbye(self, name='Noname') -> None:
#         print('Пока-Пока!', name)
#
#
# g1 = Greater()
# g1.hello('Ольга')
# g1.goodbye('Иван')
#
# g2 = Greater()
# g2.hello('Иван')
# g2.goodbye('Ольга')

# Методы классов и анализ предыдущих вызовов
# from lib import Person
#
# car = Car('Scoda', 'Oktavia', 'red')
# car.start_engine()
# car.drive_to('Город')
#
#
# p = Person()
# p.set_age(785)
# print(p.get_age())
# print(p.person_info())
#
# # Статичные члены класса
from lib import Car
#
# car1 = Car()
# car2 = Car()
# car3 = Car()
#
# print(f'В парке машин: {Car.get_counter()} шт')
#
# car = Car('Scoda', 'Oktavia')
# car.set_color('pink')
# car.start_engine()
# car.drive_to('Город')
#
# from lib import Clicker
#
# cl = Clicker()
# cl.click()
# cl.click()
# cl.click()
#
# print(cl.get_count())
# cl.reset()
# print(cl.get_count())
#
# from lib import Separator
#
# nums = Separator()
# for i in range(100):
#     nums.add_num(i)
# print(f'Список чётных чисел: {nums.get_even()}; Список нечётных чисел: {nums.get_odd()}')

s = Sorted()