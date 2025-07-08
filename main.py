# # Библиотека pymorphy
# # 1.<pip install pymorphy3> установить библиотеку
# # 2.<pip install -U pymorphy3-dicts-ru> - добавить словарь
# # морфологический анализ
# from pymorphy3 import MorphAnalyzer
#
# form = MorphAnalyzer().parse('бутылка')[0]
#
# for btl in reversed(range(99)):
#     print(f'В холодильнике {btl + 1} \
# {form.make_agree_with_number(btl + 1).word} пива')
#     print('Возьмём одну и выпьем')
#     if btl % 10 == 1 and btl != 11:
#         remain = 'Осталась'
#     else:
#         remain = 'Осталось'
#     print(f'{remain} {btl} {form.make_agree_with_number(btl).word} пива.')
#
# # Линтеры - статический анализатор кода,
# # который контролирует следование хорошим практикам
# # Flake 8
# # 1.<pip install flake8> установить библиотеку
# # 2.<pip install flake8-bugbear> - для нахождения логических ошибок
# # 3.<pip install pep8-naming> - проверяет имена на соответствие pep-8
# # настройка через Settings -> external tools
# # = Arguments: --max-complexity 10 $FileDir$/$FileName$ ; Dir: $FileDir$
# # Advanced Options/OutputFilter: $FILE_PATH$:$LINES$

# Регулярные выражения (regular expression) - поиск по строке
# r-строка = raw-string("сырая строка")
import re

pattern = r'\b\w{4}\b' # все слова из 4х символов
text_string = 'дома было холодно вечером'

result = re.findall(pattern, text_string)
print(result)

pattern = r'\d'  # все цифры от 0 до 9 () \d{3} - находит 3 цифры подряд
text_string = 'телефон 112'

result = re.findall(pattern, text_string)

# тернарный оператор работает только с выражениями и вызовом функций
# присвоение в тернарном операторе не работает
print('Цифры есть.') if result else print('Цифр нет.')

pattern = r'начало!\Z' # на что заканчивается
text_string = 'Главное - начало!'

result = re.findall(pattern, text_string)
print(result)

pattern = '[0-5][0-9]' # 2 числа подряд в нужном диапазоне
text_string = 'Время - 07:45'

result = re.findall(pattern, text_string)
print(result)

pattern = '[а-яА-Я]' # все буквы от 'а' до 'я' во всех регистрах
text_string = 'Время - 07:45'

result = re.findall(pattern, text_string)
print(result)

pattern = '[^ерм]' # исключить символы
text_string = 'Время - 07:45'

result = re.findall(pattern, text_string)
print(result)

pattern = r'\((.+?)\)' # вытащить текст из скобок
text_string = 'Поиск по образцу (pattern)'

result = re.findall(pattern, text_string)
print(result)

# Квантификаторы (quantity)
# {m} - ровно m раз
# {m,} - m раз m более
# {,n} - не более n раз
# {m,n} - от m до n раз
# ? - от 0 до 1 (аналог {0,1})
# * - от 0 до бесконечности (аналог {0,})
# + - от 1 до бесконечности (аналог {1,})

pattern = 'o{2,5}' # вытащить текст из скобок
text_string = 'Google,  Gooogle, Gooooooogle'

result = re.findall(pattern, text_string)
print(result)

pattern = 'Go{2,}gle' # вытащить текст из скобок
text_string = 'Google,  Gooogle, Gooooooogle'

result = re.findall(pattern, text_string)
print(result)
