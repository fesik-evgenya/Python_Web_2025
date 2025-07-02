# # Global and Local ( область видимости)
# # Пример как делать не надо
# a = [1,2]
#
#
# def changes_array():
#     a[0] = 0
#
# changes_array()
# print(a)


PI = 3.14

def print_array(array: list) -> None:
    for item in array:
        print(item)


def circle_length(radius: float) -> None:
    """
    расчёт длины окружности по радиусу
    :param radius: радиус окружности
    :return: длина окружности
    """
    perimetr = 2 * PI * radius
    print(f'Длина окружности с радиусом <{radius}> = {perimetr:.2f} ')


def square_area(length: int, width: int) -> None:
    """
    расчёт площади
    :param length: длина
    :param width: ширина
    :return: ничего не возвращает
    """
    area = length * width
    print(f'Площадь = {area}')


def greet(name: str) -> None:
    """
    Greeting
    :param name: Name
    :return: None
    """
    print('Привет', name)
    name = 'друг'  # переназначаем переменную!!!
    print('Здравствуй', name)


def main():
    square = 'Дворцовая площадь'
    print('Давай встретимся, где', square)
    square_area(320, 240)
    print('Ну что? Встречаемся, где', square)

    name = 'Пётр'
    greet(name)

    circle_length(5)

    words = ['Привет', 'мир']
    print_array(words)


main()