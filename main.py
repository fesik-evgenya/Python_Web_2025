# return vs yield
# разница <yield> - функция возвращает значение и продолжает работать
# создаёт генератор

def generate_list():
    for i in range(5):
        yield i  # генератор (возвращает, но не завершает)


array = list(generate_list())
print(array)

def print_goodbye(arg):
    print('Goodbye', end=' ')


def print_cruel(arg):
    print('Cruel', end=' ')


def print_world(arg):
    print('World', end=' ')


def main():
    print_goodbye(1)
    print_cruel(2)
    print_world(3)


main()

# Оператор <is>
# a is b - true будет только тогда,
# когда a и b один и тот же объект ( совпадает адрес в памяти)

a = 1
print(id(a))
a += 1
print(id(a))  # новый объёкт, который имеет новый адрес в памяти

my_fridge = ['колбаса', 'сыр', 'масло']
his_fridge = ['колбаса', 'сыр', 'масло']
print(my_fridge == his_fridge)
print(id(my_fridge) == id(his_fridge))

temp = None
print(type(temp))
print(temp is None)

def print_array(array: list, start: int = None) -> None:
    """
    Распечатываем элементы массива
    :param array: list
    :param start: index of list
    :return: None
    """
    if start is not None and start > len(array):
        return
    if start is None:
        start = 0
    for i in range(start, len(array)):
        print(array[i])


a = [1,2,3]
print_array(a)

# возврат нескольких значений из функций
# при распаковке '*' может быть только одна
def coordinates() -> tuple:
    return 5.4, 3.2


x, y, *z = coordinates()  # распаковка
print(f'х = {x}, у = {y}, z = {z}')

*names, surname = 'Остап Сулейман Бендер'.split()
print(names, surname)
# Функция с переменным числом параметров
def multy(*args):
    # print(len(args)) # подсчёт числа аргументов
    # print(args) # по индексу, либо перебором в цикле
    if not args:
        return 0
    result = 1
    for arg in args:
        result *= arg
    return result

print(multy())

# Функция со смешанным типом параметров
def multy_2(*args, first: int=0) -> int:
    """
    произведение чисел
    :param first: число
    :param args: числа, если есть
    :return: итог произведения чисел
    """
    if not args:
        return first
    result = first
    for arg in args:
        result *= arg
    return result


print(multy_2(2, 3, 4, first=5))

def calc(*args: int, operator:str ='+') -> any:
    """
    При выборе оператора производим операцию над всеми числами, которые подаём
    :param args: числа
    :param operator: оператор
    :return: результат либо сложения, либо умножения
    """
    match operator:
        case '+':
            result = 0
            for arg in args:
                result += arg
        case '*':
            result = 1
            for arg in args:
                result *= arg
        case _:
            return 'так делать нельзя'
    return result


print(calc(1, 2, 3, 4, operator='-'))

def fio (name, surname):
    return f'{name} {surname}'

print(fio(surname='Бендер', name='Остап'))  # именованные аргументы

def sandwich(type_of_meal: str, with_onion: bool=False, with_tomato: bool=False) -> None:
    print('Булочка')
    if with_onion:
        print('Кольца лука')
    if with_tomato:
        print('Ломтик томата')
    print(type_of_meal)
    print('Булочка')

sandwich('Котлета', with_onion=True, with_tomato=True)

# args = кортеж, а *kwargs больше похоже на словарь
def print_any(*args, **kwargs):
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, '=', v)


print_any('Дмитрий', 'Колесов', city='Москва', age=27)

def profile(name: str, surname: str, city: str, *children: str, **additional) -> None:
    print(f'Имя: {name}')
    print(f'Фамилия: {surname}')
    print(f'Из города: {city}')
    if len(children) > 0:
        print('Дети: ', ','.join(children))
    if 'hobbies' in additional:
        print(f'Хобби: ', ', '.split(additional['hobbies']))


profile('Дмитрий', 'Колесов', 'Волгоград',
        'Мария', 'Пётр', hobbies=['Филателия', 'Шахматы'])