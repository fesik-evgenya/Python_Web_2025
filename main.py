# ООП (inheritance)
# класс, от которого наследуем: базовый, родительский, суперкласс
# класс, который наследуется: производный, дочерний
#
#
class Rectangle:
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

# ->>>> наследование квадратом всего от прямоугольника
class Squared(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = 'Квадрат'

    def get_name(self):
        return self._name


s = Squared(5)
print(s.area())
print(s.perimetr())


