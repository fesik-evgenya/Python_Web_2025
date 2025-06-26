# цикл for
# for <переменная> in iterable:
#   команды

word = 'поток'

for ch in word:
    print(ch)

# итератор range(start, stop, step)

for i in range(2, 13, 2):
    print(i)

# если мы не используем переменную - то ставим _
for _ in range(13):
    print('Привет')


for i in range (1, 101):
    if i % 10 == 5 and i != 15:
        print(i)

# обратно проитерироваться = reversed
for i in reversed(range(1,101)):
    print(i)