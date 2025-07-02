# Функция как объект
# передаётся в другие функции, и эти функции называются -> Функция высшего порядка
# функция критерия отбора элементов списка
# Критерий: длина слова
def is_longer_six(word):
    return len(word) > 6

words = ['В', 'этом', 'списке', 'останутся', 'слова',
         'длина', 'которых', 'больше', 'шести']

for word in filter(is_longer_six, words):
    print(word)

result = list(filter(is_longer_six, words))
print(result)

fruits = ['Слива', 'Ананас', 'Апельсин', 'Малина', 'Яблоко',
         'Дыня', 'Смородина', 'Манго', 'Банан', 'Ежевика']

def find_firs_let_A(fruit: str):
    return fruit[0] == 'А'

#map
for fruit in filter(find_firs_let_A, fruits):
    print(fruit)

def square(num):
    return num ** 2


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = map(square, nums)
print(list(squares))

# превратить список num в строку цифр без пробелов (и распечатать) с помощью map()