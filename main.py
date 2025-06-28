# #Задача - исправить букву в слове сабака зная ошибку
# s = 'сабака'
# res = ''
#
# for i in range(len(s)):
#     if i == 1:
#         res += 'о'
#     else:
#         res += s[i]
#
# print(res)
#
# #Задача - исправить букву в слове сабака не зная ошибку
# s = 'сабака'
# s_right = 'собака'
# res = ''
# ind_ch_error = 'нет'
#
# for i in range(len(s)):
#     if s[i] == s_right[i]:
#         res += s[i]
#     else:
#         res += s_right[i]
#         ind_ch_error = int(i)
#
# print(f'В слове {s} ошибка в символе № {ind_ch_error + 1}. Правильное слово {res}')
#
# # Таблица символов
# s = '\xB0'  # значок градуса
# u = '\u2603'  # снеговик
#
# # две удобные функции
# # ord(символ) - возвращает код символа в Unicode
# # chr(код) - возвращает символ по Unicode-коду
#
# print(u)
# print('25' + s + 'C')
# print(f'Код снеговика в Unicode: {ord('☃')}')
# print(chr(9731))
#
# # Вывести любую фразу в шифре Unicode
# s = input('Введите фразу для зашифровки: ')
# a = set()
#
# for ch in s:
#     a.add(ord(ch))
#
# for item in a:
#     print(item, end=' ')
#
# # Обратно расшифровываем
#
# result = ''
#
# for item in a:
#     result += chr(item)
#
# print(result)
#
# # Методы строк
# abc = 'абвгдеёжзийклмнопрстуфхцшщъыьэюя'

# print(dir(abc))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix',
'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
'swapcase', 'title', 'translate', 'upper', 'zfill'
"""

phrase = 'Язык Python'

print(phrase.lower())  # все маленькие буквы
print(phrase.upper())  # все большие буквы
print(phrase.capitalize())  # только первая буква заглавная
print(phrase.title())  # Все слова с заглавной буквы
print('Ура! ' * 3)
print('Телевизор'.count('е'))  # посчитать количество нужного символа в строке
print('Python'.index('y'))  # возврат первого индекса переданного символа

# Берём строку и каждая буква повторяется столько раз на каком она месте

# for index in range(len(word := input('Введите слово: '))):
#     print(word[index] * (index + 1), end='')

# Метод strip() - убирает символы слева и справа, по умолчанию 'пробел'
# Методы lstrip() b rstrip() - тоже самое, только с одного конца

print(phrase.strip())
temp = int(input('Введите количество: ').strip())
print(temp)

# Шифр Цезарь - ДЗ на выходные
# сдвигает на какое-то количество нумерацию в символах
# расшифровать и зашифровать
# E - расшифровать, D - зашифровать, Q - выход из программы

# abc = 'абвгдеёжзийклмнопрстуфхцшщъыьэюя'