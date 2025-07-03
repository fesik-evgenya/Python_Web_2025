# частотность слов
ENGLISH_ABC = [chr(ch) for ch in range(ord('a'), ord('z') + 1)]
RUSSIAN_ABC = set([chr(ch) for ch in range(ord('а'), ord('я') + 1)] + ['ё'])
ABC = (set(ENGLISH_ABC) ^ set(RUSSIAN_ABC) ^
       set(map(lambda x: x.upper(), ENGLISH_ABC)) ^
       set([x.upper() for x in RUSSIAN_ABC]))

print(ENGLISH_ABC)
print(RUSSIAN_ABC)
print(ABC)

txt = """Может, нас троих что-то связывало в прошлой жизни, иначе откуда во мне
 эта страсть к путешествиям? Урал, Сибирь, Камчатка, Сахалин,
 средневековые замки Испании, древние дороги Японии… В самих названиях
 мне слышится как будто зов Земли. Значит, Земля зовёт меня полюбоваться
 ею и открывает новые бездны и выси. """

text = ''.join(filter(lambda x: x in ABC ^ {' '}, txt))
print(txt)

def remove_punc (text: str) -> str:
    return ''.join(filter(lambda x: x in ABC ^ {' '}, text))


print(remove_punc(txt))

def get_words(text: str) -> list:
    return remove_punc(text).split()


def long_words(text: str, length:int=4) -> list:
    return list(filter(lambda x: len(x) >= length, get_words(text)))


print(long_words(txt))

# частотный анализ слов с помощью словарного выражения
d = {}
words = get_words(txt)

for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

res = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
print(res)

# сортировка списка списков
goods = [
    ['Утюг', 1500, 2],
    ['Фен', 1200, 5],
    ['Телевизор', 8000, 3]
]
print(sorted(goods, key=lambda s: (s[1], s[2], s[0])))  # сначала по цене, потом по количеству, потом по алфавиту

# проверка коллекций
# All() Any() - применяется ко всем итерируемым объектам
# Any -> любой элемент коллекции, то тогда True
# All -> все элементы коллекции, то тогда True

print(all([1, 2, 3]))  # все элементы ненулевые, поэтому вернёт True
print(all([1, 2, 0]))  # 1 элемент нулевой, поэтому вернёт False
print(all([]))  # почему-то возвращает True

words = 'один два три'.split()
print(all(list(map(lambda x: len(x) > 3, words))))

# Потоковый ввод - sys.stdin - это итератор (подобно range), но только в одну сторону
# CTRL + D -> запуск в командной строке
import sys

data = [d.strip('\n') for d in sys.stdin.readlines()]
print(data)
