# break - принудительное прерывание цикла
# continue - принудительное прерывание текущей итерации и начать следующую


# break
num = 3
print('Я загадал число, угадай!')

while True:
    var = int(input('Ваше значение: '))
    if var == num:
        print('Ура. Угадал!')
        break
    elif var > num:
        print('Число больше загаданного!')
    else:
        print('Число меньше загаданного!')

print('Приходи ещё!')

# continue
counter = 0
# цикл из 5 итераций, но 3ю пропускаем
while counter < 5:
    counter += 1  # инкремент
    if counter == 3:
        continue
    print(f'Итерация номер {counter}')

