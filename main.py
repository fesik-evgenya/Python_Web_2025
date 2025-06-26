# min, max, average, summ, production
N = 5
total = 0
prod = 1
min_val = float('inf') # + бесконечность
max_val = float('-inf') # - бесконечность
average = 0

for _ in range(N):
    num = int(input('Введите целое число: '))
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    total += num
    prod *= num
    average = total / N

print(f'Сумма: {total}')
print(f'Произведение: {prod}')
print(f'Ср арифметическое: {average}')
print(f'Минимальное число: {min_val}')
print(f'Максимальное число: {max_val}')

# факториал
N = 5
fact = 1

for i in range(1,N+1):
    fact *= i

print(fact)