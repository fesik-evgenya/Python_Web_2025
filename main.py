# Коллекции = (set, list, dict, tuple)
# Множества - Set ()
# Может хранить разные типы данных
# Неупорядоченная коллекция данных
# Множество убирает повторы автоматом

s = set()  # пустое множество
print(dir(s))  # - список методов множества

s = {'3', '5', '7', '3', '3'}

s.add('8.5')  # добавление нового элемента

s.remove('3')  # удаление элемента -> вызывает ошибку, если элемента нет в множестве
s.discard('3')  # удаление элемента в слепую
temp = s.pop()  # удаление случайного элемента с возвратом значения
print(temp)

print(type(s)) # узнать класс объекта

print(f'Число элементов в s = {len(s)}')

print('Присутствует ли 3')
if str(3) in s:
    print('Да')
else:
    print('Нет')

for item in s:
    print(item)
print(s)

s.clear()  # удаление всех элементов из множества

# 'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard',
# 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset',
# 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union',
# 'update'