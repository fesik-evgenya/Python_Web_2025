# Методы строк - часть 2
# Начало т окончание строки
# startswith и endswith
from itertools import count

s = 'Cмотреть'

if s.lower().startswith('смо'):
    print('Да')

if s.endswith('еть'):
    print('Да')

# find('подстрока', 'start', 'end')
# возвращает первое вхождение искомой подстроки
# возвращает (-1) - значит не найдено


s = 'Смотреть, вертеть, видеть'

index = s.find('еть')  # с начала строки
print(index)

index = s.find('еть', 10)  # с позиции старт
print(index)
index = s.find('еть')
print(index)

s = 'синхрофазотрон'  # ищем 'о': сколько их и где находятся
ch = 'о'

if ch in s:
    count = s.count(ch)
    print(f'Буква \'{ch}\' встречается в слове "{s}" {count} раз(а).')
    print('Её позиция/позиции:', end=' ')
    start = 0
    for i in range(count):
        pos = s.find(ch, start)
        start = pos + 1
        print(pos, end=' ')
else:
    print(f'Буквы \'{ch}\' нет в слове "{s}".')
