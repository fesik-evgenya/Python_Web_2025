# Циклы:
# while
# while <условие>:
#     команды
# for
counter = 0  # обнуляем счётчик

# цикл из 5 операций
while counter < 5:
    print(f'Итерация номер {counter + 1}')
    counter += 1  # инкремент

print(f'Итого в counter уже {counter}')
print(f'Обратный отсчёт:')

while counter > 0:
    print(f'Итерация номер {counter}')
    counter -= 1  # декремент