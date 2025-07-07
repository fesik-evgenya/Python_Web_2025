# Файлы - это набор данных, сохраненный на носителе, содержащий
# имя и расширение ( которое связывает с исполняющей программой)
# Два типа в питоне = t - текстовые и p - бинарные(jpg, avi, mp3)
# w - write (запись, создаётся), но всё что было до этого - стирается
# a - append (запись идёт в конец)
# r - читать (файл должен существовать)
# одновременно читать и записывать нельзя!!! только по очереди - открыл, закрыл
# Открытие с менеджером контеста

# проследит что бы файл закрылся - тот файл который успешно открылся.
with open('info.txt', 'wt', encoding='utf-8') as fo:
    text= fo.read()
    lst = text.splitlines()
    print(lst)

print(fo.mode)
print(fo.name)
print(fo.encoding)

count = fo.write('Этот текст будет в файле!')
print('В файл записано', count, 'байт!')
fo.close()

fo = open('info.txt', 'rt', encoding='utf-8')

# каждый раз read начинает читать с того места, гед остановился в прошлый раз
text = fo.read(11)  # на вход принимает сколько байт читать
fo.read(6)
text += fo.read(7)

print('Вот, что было в файле', end=': ')
print(text)

fo.close()

# добавляем текст в конец файла
fo = open('info.txt', 'at', encoding='utf-8')

# fo.write(' Хороший текст.')
print('\nА вот это будет уже с новой строки.', file=fo)
print('\nВот ещё одна строка.', file=fo)
fo.close()

fo = open('info.txt', 'rt', encoding='utf-8')
text = fo.readline()
print(text)

# построчное чтение №1
while text := fo.readline():
    print(text.rstrip('\n'))

# построчное чтение №2
lst = fo.readlines()
lst = list(map(lambda x: x.strip('\n'), lst))
print(lst)

# построчное чтение №3
text = fo.read()
lst = text.splitlines()
print(lst)

fo.close()

