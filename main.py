# Полиморфизм + Утиная типизация
# следим как на уровне синтаксиса и на уровне смысла
# <isinstance(объект, тип)> -> True способ узнать тип возвращаемых из класса данных

from lib import Squared, Circle, Rectangle
# 1й способ
# def shape_info(shape):
#     print(f' Площадь фигуры "{shape.get_name()}": {shape.area()}, Периметр: {shape.perimetr()}')

# 2-й способ
r, c, s = 'прямоугольник', 'круг', 'квадрат'

def shape_info(shape: object):
    if isinstance(shape, Circle):
        fig = c
    elif isinstance(shape, Rectangle):
        fig = r
    elif isinstance(shape, Squared):
        fig = s

    print(f' Площадь фигуры "{fig}": {shape.area()}, Периметр: {shape.perimetr()}')

s = Squared(10)
shape_info(s)

cr = Circle(10)
shape_info(cr)

r = Rectangle(5,2)
shape_info(r)

from lib import Student, Person, Employee

people = [
    Person('Александр', 27),
    Student('Дмитрий', 18,'ГУАП'),
    Employee('Пётр', '26', 'Авангард')
]
for person in people:
    if isinstance(person, Student):
        print(person.get_university())
    elif isinstance(person, Employee):
        print(person.get_company())
    else:
        print(person.get_name())
from lib import Selector

lst = list(range(1, 15))

s = Selector(lst)

print(s.get_odd())
print(s.get_even())

from lib import Calc

lst = list(range(1, 15))
lst += '15'
nums = Calc(lst)

print(nums.get_avg())

# OOП (magic methods) = как пример "str(a) -> a.__str__()"
# abs() - абсолютное значение, без минусов

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __str__(self):
        return f'<Point: ({self._x}, {self._y})>'

    def __repr__(self):
        return f'<List of Point: ({self._x}, {self._y})>'

    def __sub__(self, other):
        return Point(abs(self._x - other._x), abs(self._y - other._y))

    def __add__(self, other):
        return round(((self._x - other._x) ** 2  + (self._y - other._y) ** 2) ** 0.5)



p1 = Point(5, 4)
p2 = Point(10, 2)
print(p1 - p2)
print(f'Приближённое расстояние между двумя точками: {p1 + p2}')
