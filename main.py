# превратить список num в строку цифр без пробелов(и распечатать) с помощью map()

def square(num: int) -> str:
    """
    возводит в квадрат и переводит в строку
    :param num: число
    :return: число в квадрате типа строка
    """
    return str(num ** 2)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(square, nums)

print(*list(squares), sep='')

# Критерий - вхождение подстроки
# в частности 'ан'
fruits = ['Слива', 'Ананас', 'Апельсин', 'Малина', 'Яблоко',
         'Дыня', 'Смородина', 'Манго', 'Банан', 'Ежевика']

def string_contain(s):
    return 'ан' in s

res = list(filter(string_contain, fruits))
print(res)
