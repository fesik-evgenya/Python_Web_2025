## Анонимные функции
## lambda-функции
## lambda <аргументы>: выражения
#
## Функция критерия отбора элементов списка
## Критерий - первая буква
# is_first_letter_a = lambda  word: word[0] == 'а'
#
# string_contains = lambda s: 'ан' in s
#
# fruits = ['Слива', 'Ананас', 'Апельсин', 'Малина', 'Яблоко',
#          'Дыня', 'Смородина', 'Манго', 'Банан', 'Ежевика']
# result = list(filter(lambda fruit: len(fruit) > 6, fruits))
# result_first_letter = list(filter(lambda fruit: fruit[0] == 'А', fruits))
# result_contain_ch = list(filter(lambda word: 'ан' in word, fruits))
#
# print(result)
# print(result_first_letter)
# print(result_contain_ch)
#
# print(list(map(lambda x: x ** 2, range(3, 16))))  # то же самое =>
# print([i ** 2 for i in range(3, 16)])
#
# words = ['В', 'этом', 'списке', 'останутся', 'слова',
#          'длина', 'которых', 'больше', 'шести']
# long_words = [word for word in words if len(word) > 6]
# print(long_words)
#
ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSSIAN_ABC = set([chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё'])
ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
       set(map(lambda x: x.upper(), ENGLISH_ABC)) ^
       set([x.upper() for x in RUSSIAN_ABC]))
#
# print(ENGLISH_ABC)
# print(RUSSIAN_ABC)
# print(ABC)

txt = """Может, нас троих что-то связывало в прошлой жизни, иначе откуда во мне
 эта страсть к путешествиям? Урал, Сибирь, Камчатка, Сахалин, 
 средневековые замки Испании, древние дороги Японии… В самих названиях 
 мне слышится как будто зов Земли. Значит, Земля зовёт меня полюбоваться 
 ею и открывает новые бездны и выси. """
#
# text = ''.join(filter(lambda x: x in ABC ^ {' '}, txt))
# print(txt)
#
def remove_punc (text: str) -> str:
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))
#
#
# print(remove_punc(txt))

def get_words(text: str) -> list:
    return remove_punc(text).split()


def long_words(text: str, length:int=4) -> list:
    return list(filter(lambda x: len(x) >= length, get_words(text)))


# print(long_words(txt))

# Словарные выражения
# словарь квадратов чётных чисел до 10 включительно
squr_even = {n: n ** 2 for n in range(2, 11, 2)}
print(squr_even)
# умножаем каждое значение в словаре на 2
souse_dict = {
    'x': 1,
    'y': 1,
    'z': 1,
}

dest_dict = {k: v * 2 for k, v in souse_dict.items()}
print(dest_dict)
