import sys

strings = [d.strip('\n') for d in sys.stdin.readlines()]
length =len(strings)  # определяем сколько было строк
rem = length % 3  # спрашиваем делиться ли на 3

if rem:
    strings = strings[:length - rem]    # отрезаем

for x in range(0, length - rem, 3):  # просто перебираем тройки строк
    summ = sum(len(a) for a in strings[x:x + 3])  # сумма длин всех строк тройки слов
    result = []
    for s in strings[x:x + 3]:
        temp = s.lower().split()
        # фильтрация списка temp по кратности длины в соотношении
        result += filter(lambda  a: len(a) % 2 == summ % 2, temp)
    result = sorted(set(map(lambda b: b.capitalize(), result)))[:5]

print(*result, sep='. ')

