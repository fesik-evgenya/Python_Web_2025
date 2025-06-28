# Строки (immutable, iterable)
# итерируемый, но не изменяемый объект

s = ''
print(id(s))  # узнать адрес в памяти
s += 'Привет'
print(id(s))
print(s)


s = 'Python'
# s[3] = 'y' error / не позволяет менять символы в строке (immutable)
print(s[-1])  # выведет последний символ
print(s[0])  # выведет первый символ
print(f'Длина слова: {len(s)}')


main_str = 'язык питон'

total_Vw_Str = 0
for s in main_str:
    if s in {'а', 'о', 'я', 'и', 'ю', 'э', 'ы', 'е', 'у'}:
        total_Vw_Str += 1
print(f'В строке всего {total_Vw_Str} гласных(е) буквы')

# Перебор строки по числовому индексу
for index in range(len(main_str)):
    print(main_str[index])