# Списочные выражения (list comprehension)
# squares = []
# for i in range(10):
#     squares.append(i ** 2)
#
# на первом месте мы пишем что попадет в список,
# а на втором месте по какой закономерности,
# а на третьем месте условие какие нужны ( например чётные через If)

squares = [i ** 2 for i in range(10)]
print(*squares, sep=', ')

# список квадратов чётных чисел
squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(*squares, sep=', ')

# произведение i и j
print(*[i * j for i in range(3) for j in range(3)], sep='\n')

# получить список целых чисел
n = '500 600 700 800'
print([int(i) for i in n.split()])

# проверить список на вхождение в другой
n = '100 200 300 400 500 600 700 800 900'
approved = [500, 800]
a = [int(i) for i in n.split() if int(i) in approved]

print(a)

# нужно составить список из каждого 3го слова данного текста
# (с помощью списочного выражения)
text = 'Списочные выражения применяются для эффективности кода'.split()

lst_result = [text[i] for i in range(2,len(text),3)]  # [a for a in text.split()[2::3]]
print(lst_result)

# Вложенные списки - table, matrix
table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

table = [[1] * 3 for _ in range(3)]

# Наполнение матрицы
matrix = []
table = []
start = 1
N = 4

for i in range(N):
    table =[]
    for j in range(start,start+N):
       table.append(j)
    start += N

print(matrix)
# генерация матрицы через списочное выражение
N = 3
matrix = [[i + j for j in range(N)] for i in range(1, 10, N)]
print(matrix)

