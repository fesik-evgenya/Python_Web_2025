# # Функции (DRY - повторяй себя) - может возвращать результат, а может и нет
# # это какой-то алгоритм помещается в капсулу с каким то наименованием
# # определяется один раз, но ссылается многократно
# # определяют функцию с параметром, а вызывают с аргументом
# # если функция ни чего не возвращает то это процедура ( просто набор команд)
# # scope (область видимости) - local и global - лучше когда local
# # в функцию передаётся копия значения, сама глобальная переменная на функцию не влияет
# #
# # синтаксис:
# # def <имя функции>([параметры]):
# #     команды
#
# person = 'Пётр'  # глобальная переменная
# count = 0
#
#
# def greet_to_name(name='noname'):
#     print('Привет', name)
#     print(count)
#
#
# def increment():
#     global count
#     count += 1
#
#
# def print_list(array=None):
#     if array is None:
#         array = []
#     for item in array:
#         print(item)
#
#
# increment ()
# greet_to_name()
# print_list(['Мяу', 'Гав'])

# Return Value в Функции
def square(num):
    return num ** 2

def even_odd(num):
    if num % 2 == 0:
        return 'Чётное'
    return 'Нечётная'


def print_string(s=None):
    if s is None:
        return
    print(s)

t = square(5)
print(t)
print(even_odd(5))