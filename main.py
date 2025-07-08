# Исключение - аварийная остановка программы (runtime)
# try:
#     что пытаемся сделать
# except:
#     обрабатываем исключения
# finally:
#     выполняется в любом случае
# <NameError> - исключение, которое связано с необъявленной переменной

flag = False  # открывался ли на запись файл

try:
    fo = open('information.txt', encoding='utf-8')

except FileNotFoundError:
    fo = open('information.txt', 'wt', encoding='utf-8')
    flag = True
    print('Фал не обнаружен и создан с параметрами по умолчаниями')
    # with open('information.txt', 'wt', encoding='utf-8') as fo:
    #     fo.write('по умолчанию')

else:
    print('Файл открыт успешно. Читаем его и закрываем.')
    print(fo.read())
    fo.close()

finally:
    if flag: # если было исключение и фал был открыт для записи
        fo.write('по умолчанию')
        fo.close()
    print('Продолжаем работать.')

print('Остаток от деления: ')

try:
    value = int(input('На что делим число 10: '))
    res = 10 % value
    print(f'Остаток от деления 10 на {value} = {res}')

# исключение деления на ноль
except ZeroDivisionError:
    print('На ноль делить нельзя!')

except ValueError:
    print('Надо вводить только целые числа!')

# вернуть инфу что за исключение произошло
except Exception as exp:
    print('Произошло исключение: ', exp.__class__.__name__,'=', exp)

# тоже в цикле - пока пользователь не введёт правильную инфу
print('Остаток от деления: ')
flag = True

while flag:
    try:
        value = int(input('На что делим число 10: '))
        res = 10 % value
        print(f'Остаток от деления 10 на {value} = {res}')

    except ZeroDivisionError:
        print('На ноль делить нельзя!')

    except ValueError:
        print('Надо вводить только целые числа!')

    except Exception as exp:
        print('Произошло исключение: ', exp.__class__.__name__,'=', exp)

    else:
        flag = False

# "Бросаемся" исключениями - raise
max_val = 10
min_val = 1

try:
    val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
    if not min_val < val < max_val:
        raise ValueError('Введённое число вне диапазона')
    print(f'Введённое число {val} лежит в заданном диапазоне')
except ValueError as exp:
    print('Надо быть внимательнее:', exp)

# Утверждения (assertions) - в продакшине не используется, только в тестировании
try:
    text = input('Введите текст: ')
    assert len(text) > 3  # это утверждение
except AssertionError:
    print('Слишком короткий текст')

# Задача 1.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
loop = True

while loop:
    try:
        ind = int(input(f'Ведите индекс(целое число) в диапазоне от 0 до {len(lst)-1}: '))
        print(f'Число по индексу [{ind}]: {lst[ind]}')

    except IndexError:
        print(f'Индекс должен быть до {len(lst)-1}.')

    except ValueError:
        print(f'Индекс должен быть целым числом!')

    except KeyboardInterrupt:
        print(f'Программа остановлена')
        break

    except Exception as exp:
        print('Произошло исключение: ', exp.__class__.__name__,'=', exp)

    else:
        loop = False

# Задача 2.
loop = True

while loop:
    try:
        a = int(input('Введите число <a>: '))
        b = int(input('Введите число <b>: '))
        print(f'Итог деления {a} на {b}: {a / b}')

    except ZeroDivisionError:
        print('На ноль делить нельзя!')

    except ValueError:
        print('Необходимо ввести число!')

    except Exception as exp:
        print('Произошло исключение: ', exp.__class__.__name__, '=', exp)

    except KeyboardInterrupt:
        print('Выполнение программы прервано. Запустите программу снова.')
        break
    else:
        loop = False