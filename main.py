#  Iterable object
#  len() - длина итерированного объекта
word = input('Введите слово для анализа: ')

if not  word or len(word) < 4:
    print('Вы ничего не ввели или слово слишком короткое')
else:
    print(f'''Длина слова "{word}" = {len(word)}''')  # c f-строками
    print('Длина слова "'+ word + '" =', len(word))  # по лайтовому