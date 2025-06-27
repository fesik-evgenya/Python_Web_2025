# Города - проверка был ли город уже назван

s = set()

while (city := input('Назовите город: ')):
    if city in s:
        print('Город уже был!')
    else:
        s.add(city)

print(f'Итого было названо: {len(s)} городов(а):')
for item in s:
    print('\t', item)