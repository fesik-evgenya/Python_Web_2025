# Кортеж ( tuple, immutable ) - такой же список, но не изменяемый
# в памяти занимает меньше места и обращение к нему быстрее
BLACK = (0, 0, 0)  # константа

empty = () #tuple()
one = (1,)  #tuple()
temper = 36,6  #tuple()
s = 'Python'
t = tuple(s) + ('.',)
print(t)

# 'count', 'index'

cards = [(7, 'червей'),('туз', 'пик'),('дама', 'бубей')] # список кортежей

print((1, 2) <= (2, 1))  # сравнение кортежей

# распаковка списков с помощью кортежей (работает со строками и множествами)
# !!! количество переменных должно быть равно кол-ву элементов

channels = ['red', 'green', 'blue']

r, g, b = channels  # распаковка

print(r)

r, *other = channels # частичная распаковка

print(other)

first, second = input(), input()
print(first, second)

# список студентов со средними баллами
N = 3
lst_students = []

for _ in range(N):
    person , avr_score = input('Фамилия: '), float(input('средний балл: '))
    lst_students.append((person, avr_score))

print(lst_students)

for st in lst_students:
    person, avr_score = st
    print('Студент: ', person)
    print('Средний балл', avr_score)

# функция sorted() - что бы не подали ей на вход, она вернёт отсортированный список

s = {'Петров', 'Иванов', 'Сидорова'}

lst = sorted(s, reverse=True)
print(*lst, sep=', ')

# функция enumerate возвращает в цикле 'for' пару(индекс и значение) в кортеже

fio = ['Сидорова', 'Петров', 'Иванов']

for i, v in enumerate(fio):
    print(f'{i + 1}.{v}.')
