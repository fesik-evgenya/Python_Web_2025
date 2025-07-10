class Balance:
    def __init__(self):
        self._right = 0
        self._left = 0

    if __name__ == '__main__':
        print('для проверки работы весов запустите файл balance_demo.py')

    def add_left(self, weight: int) -> None:
        """
        Добавляет вес в левую чашу
        :param weight: вес, кладомый в левую чашу
        :raises ValueError: если вес отрицательный
        """
        if weight < 0:
            raise ValueError('Снятие веса не поддерживается в текущей версии')
        self._left += weight

    def add_right(self, weight: int) -> None:
        """
        Добавляет вес в левую чашу
        :param weight: вес, кладомый в правую чашу
        :raises ValueError: если вес отрицательный
        """
        if weight < 0:
            raise ValueError('Снятие веса не поддерживается в текущей версии')
        self._right += weight

    def result(self) -> str:
        """
        Возвращает результат взвешивания, согласно заданию
        :return: текстовое сообщение о том, какая чаша перевесила
        """
        return 'весы в равновесии' if self._is_balanced() \
            else 'левая чаша перевесила' if self._left > self._right \
            else 'правая чаша перевесила'

    def reset(self) -> str:
        """
        Опустошает обе чаши весов
        :return: сообщение о том, что весы обнулены
        """
        self._left = 0
        self._right = 0
        return 'весы сброшены'

    def get_status(self) -> str:
        """
        Сообщает текущее состояние весов
        :return: текстовое сообщение о весе на обеих чашах
        """
        return f'на левой чаше {self._left}, на правой чаше {self._right}'

    def get_difference(self) -> int:
        """
        Возвращает разницу веса между чашами весов
        :return: положительное число, если левая чаша тяжелее,
                отрицательное число, если правая чаша тяжелее,
                0, если весы в равновесии
        """
        return self._left - self._right

    def get_difference_percentage(self) -> float:
        """
        Возвращает в процентах от веса более лёгкой чаши,
        на сколько вторая чаша тяжелее.
        :return: положительное число, если левая чаша тяжелее,
                отрицательное число, если правая чаша тяжелее,
                0, если весы в равновесии
        """
        if self._is_balanced():
            return 0.0
        havier_scale = max(self._left, self._right)
        lighter_scale = min(self._left, self._right)
        if lighter_scale == 0:
            return float('inf') if self._left > self._right else -float('inf')
        ratio = ((havier_scale / lighter_scale) - 1) * 100
        return ratio if self._left > self._right else -ratio

    def _is_balanced(self) -> bool:
        """
        Проверяет, находятся ли весы в равновесии
        :return: ИСТИНУ, если весы в равновесии, ЛОЖЬ в противном случае
        """
        return self._left == self._right

class Sorter:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def result(self):
        # список слов, отсортированный по длине
        return sorted(self.words, key=lambda x: len(x), reverse=True)


class Separator:
    def __init__(self):
        self.odd = []
        self.even = []  # чётные

    def add_num(self, num):
        if num % 2:
            self.odd.append(num)
        else:
            self.even.append(num)

    def get_odd(self):
        return self.odd

    def get_even(self):
        return self.even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_counter(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    counter = 0  # статичное свойство (счетчик машин)

    def __init__(self, brand='Noname', model='NoModel', color='black'):
        self.brand = brand  # 'Skoda'
        self.model = model  # 'Octavia'
        self.color = color  # 'red'
        self.engine_on = False
        Car.counter += 1

    def start_engine(self):
        self.engine_on = True

    def drive_to(self, place):
        if self.engine_on:
            print(f'Едем в {place} на {self.brand} {self.model}')
        else:
            print('Двигатель не заведён, не едем')

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Bill', age=1):
        # свойства (поля) класса
        self._name = name
        self._age = age

    # setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print('Некорректный возраст — ', new_age)

    # getters
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def person_info(self):
        print(f'Человек с именем {self._name}. Возраст: {self._age}')


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это библиотека, а исполняемый - main.py')