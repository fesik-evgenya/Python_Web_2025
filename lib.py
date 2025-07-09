class Balance:
    def __init__(self) -> None:
        self._right = 0
        self._left = 0

    def add_left(self, weight: int) -> None:
        self._left += weight

    def add_right(self, weight: int) -> None:
        self._right += weight

    def result(self) -> str:
        return 'Левая перевесила' if self._left > self._right \
            else 'Правая перевесила' if self._left < self._right \
            else 'Достигнут баланс'

class Sorted:
    def __init__(self):
        self._words = []

    def add_word(self, word: str):
        self._words.append(word)

    def result(self):
        return sorted(self._words, key=lambda x: len(x), reverse=True)


class Separator:
    def __init__(self):
        self._odd = []
        self._even = []

    def add_num(self, num):
            self._even.append(num) if not num % 2 else self._odd.append(num)

    def get_odd(self):
        return self._odd

    def get_even(self):
        return self._even


class Clicker:
    def __init__(self):
        self._counter = 0

    def click(self):
        self._counter += 1

    def get_count(self):
        return self._counter

    def reset(self):
        self._counter = 0


class Car:
    counter = 0  # статичное свойство (счетчик)
    def __init__(self, brand='No Brand', model='No Model', color='black'):
        self._brand = brand
        self._model = model
        self._color = color
        self._engine_on = False
        Car.counter += 1

    def start_engine(self):
        self._engine_on = True  # пока не сработает

    def drive_to(self, place):
        if self._engine_on:
            print(f'Едем в {place} на {self._brand} {self._model} цвета {self._color}')
        else:
            print('Двигатель не заведён, не едем!')

    # getters
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    # setters
    def set_brand(self, new_brand):
        if new_brand:
            self._brand = new_brand

    def set_model(self, new_model):
        if new_model:
            self._model = new_model

    def set_color(self, new_color):
        if new_color:
            self._color = new_color

    @staticmethod
    def get_counter():
        return Car.counter


class Person:
    def __init__(self, name='Bill', age=1):
        self._name = name
        self._age = age

    # setters
    def set_name(self, new_name):
        if new_name:
            self._name = new_name

    def set_age(self,new_age):
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
        return f'Человек с именем {self._name}. Возраст: {self._age}'


def summ(a, b):
    return a + b


def diff(a, b):
    return a - b


if __name__ == '__main__':
    print('Это библиотека, а исполняемый - main.py')