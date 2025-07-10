# ООП (inheritance)
# класс, от которого наследуем: базовый, родительский, суперкласс
# класс, который наследуется: производный, дочерний

# class Rectangle:
#     def __init__(self, wight, height):
#         self._wight = wight
#         self._height = height
#         self._name = 'Прямоугольник'
#
#     def perimetr(self):
#         return 2 * (self._wight + self._height)
#
#     def area(self):
#         return self._wight * self._height
#
#     def get_name(self):
#         return self._name
#
# # ->>>> наследование квадратом всего от прямоугольника
# class Squared(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self._name = 'Квадрат'
#
#     def get_name(self):
#         return self._name
#
#
# s = Squared(5)
# print(s.area())
# print(s.perimetr())
from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    def info(self):
        print(f'Класс: {self.__class__.__name__}')

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetr(self):
        pass


class Rectangle(Shape):
    def __init__(self, wight, height):
        self._wight = wight
        self._height = height
        self._name = 'Прямоугольник'

    def perimetr(self):
        return 2 * (self._wight + self._height)

    def area(self):
        return self._wight * self._height

    def get_name(self):
        return self._name


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius
        self._name = 'Круг'

    def perimetr(self):
        return round(2 * pi * self._radius)

    def area(self):
        return self._radius ** 2

    def get_name(self):
        return self._name


# ->>>> наследование квадратом всего от прямоугольника
class Squared(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = 'Квадрат'

    def get_name(self):
        return self._name


class Triangle(Squared):
    def __init__(self, side):
        super().__init__(side)
        self._side = side
        self._name = 'Треугольник'

    def area(self):
        return round((3 ** 0.5 * self._side ** 2) / 4)

    def perimetr(self):
        return self._side * 3


s = Triangle(5)
print(s.area())
print(s.get_name())

# ОПП Class
class BankAccount:
    def __init__(self, name, surname):
        self._owner_name = name
        self._owner_surname = surname
        self._balance = 0

    def on_deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'Депозит пополнен на сумму {amount}')
        else:
            return f'Сумма не может быть отрицательной'

    def with_draw(self, amount):
        if 0 < amount < self._balance:
            self._balance -= amount
            print(f'С депозита снята сумма {amount}')
        else:
            return f'Не хватает средств. Over Draft не доступен'

    def get_balance(self):
        return self._balance


client = BankAccount('Евгения', 'Петрова')
client.on_deposit(500)
client.with_draw(400)
print(client.get_balance())

# # Home Task
# """
# Задача: смоделировать зоопарк с разными животными
# Условия:
# Базовый класс Animal с методом make_sound()
# Классы-наследники: Dog, Cat, Elephant с переопределнием звуков.
# Класс Zoo хранит список животных и метод make_all_sound
#
# """
#
# class Animal:
#     def __init__(self):