# Операции над множествами
a = {3, 5, 7, 8}
b = {3, 5, 7, 9, 11}

# Объединение множеств
c = a.union(b)  # c = a / b (идентичная запись)
print(c)

# Пересечение множеств
c = a.intersection(b)  # c = a & b (идентичная запись)
print(c)

# Разность множеств - есть в первом, но нет во втором
c = a.difference(b)  # c = a - b (идентичная запись)
print(c)

# Симметричная разность множеств - вся разница от каждого множества вместе
c = a.symmetric_difference(b)  # c = a ^ b (идентичная запись)
print(c)

# Удаление всех карт, кроме туза = Пример
cards = {3, 7, 'T', 'D', 'V', 'K'}
ace = {'T'}

result = cards - ace
print(result)

# 2 вариант
cards = {3, 7, 'T', 'D', 'V', 'K'}
t_is = False

while cards:
    card = cards.pop()
    if card == 'T':
        cards.add(card)
        t_is = True
    else:
        print(cards)

    if t_is and len(cards) == 1:
        break
