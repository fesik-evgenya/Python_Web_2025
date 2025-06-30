# Списки (list) - изменяемая последовательность данных
# может состоять из смешанных типов данных

s = {'3', '4', '5'}
lst = list(s)
lst = list('Python')
lst = list(range(1,11))
lst = []  # пустой список
lst = [1, 2, 3]
lst = [1, 2, 3] * 3  # по аналогии со строками

print(lst)

# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

s = 'сабака'
lst = list(s)

lst[1] = 'о'
print(lst)

# append() - добавляет в конец списка значение
s = []
for i in range(11):
    s.append(i)

print(s)

# extend() - расширяет список на значение ( например другой список
s1 = [1, 2, 3]
s2 = [4, 5, 6]

s3 = s1.extend(s2).copy()

print(s1.extend(s2))  # или s1 + s2
print(s3)

lst = list(range(10))
sls = lst[2::2]

print(sls)

for i in range(0, len(lst), 2):
    print(lst[i], '-', lst[i] ** 2)

del lst[2]  # удалить элемент(грубо)

# remove() - удаляет первое значение в списке
#
# pop() - забирает из списка по индексу значение, и возвращает его же.
# по дефолту последний индекс списка
#
# sort() - сортировка списка. по умолчанию reverse = False
# если нужно отсортировать от большего к меньшему - reverse = True.

a = ['a', 'b', 'c']
b = a  # не копируем, а всего лишь делаем ссылку на изначальную область памяти
b.append('d')

print(id(a))
print(id(b))
print(a)
print(a)

b = a[:]  # a.copy() - создаём новую ячейку памяти с данными

lst_for_okroshka = []  # пустой список
# набираем ингредиенты
while (item := input('Какой ингредиент добавляем?: ')) != '':
    lst_for_okroshka.append(item)
# переводом в множество и обратно убираем дубляжи ввода
temp = set(lst_for_okroshka)
lst_for_okroshka = list(temp)

print (f'\n\tУ нас есть {len(lst_for_okroshka)} ингредиента(ов): ')
# сортируем по алфавиту
lst_for_okroshka.sort()
# распечатываем список ингредиентов
for i in range(len(lst_for_okroshka)):
    print(f'\t{i+1}. {lst_for_okroshka[i]}')

# реализовываем стек по книгам
lst_books = []

while (book := input('Положите книгу в стопку: ')) != '':
    lst_books.append(book)


while (answer := input('Хотите забрать книгу? (нет/да): ')) == 'да' or not lst_books:
    print(f'Вы взяли книгу: {lst_books.pop()}')

# распаковка списка через * в print()
lst_words = []
result_str = ''

while (word := input('Введите слово: ')).strip() != '':
     lst_words.append(word[0].upper())

print('Получилась аббревиатура: ', end=': ')
print(*lst_words, sep='')