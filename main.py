# Формат вывода 2

name = 'Игорь'
email = 'aaa@bbb.ru'
age = 32

# 1 способ (плейсхолдеры)
# %s - string
# %d - digit (целое число)
# %f - float
print('Имя: %s, E-mail: %s, Возраст: %d' % (name, email, age))

#2 способ c помощью формата
print('Имя: {}, E-mail: {}, Возраст: {}'.format(name, email, age))

#3 F - строки
print(f'Имя: {name}, E-mail: {email}, Возраст: {age}')



name = 'Игорь'
email = 'aaa@bbb.ru'
weight = 56.300

print(f'Имя: {name}, E-mail: {email}, Возраст: {weight:6.2f}')