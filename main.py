# читаем файл и вытаскиваем информацию,
# убираем повторы и делаем сортированный список
res = []

with open('./docs/list.txt', 'rt') as f:
    while temp := f.readline().rstrip('\n'):
        res += temp.split(', ')

# res = list(map(lambda x: x.rstrip('\n'), res))
res = sorted(int(x) for x in set(res))

print(res)