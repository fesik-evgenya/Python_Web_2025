# JSON - (Java Script Object Notation)
# для чтения из файла- load()
# читает строковое представление - loads()
import json

with open('dogs.json', 'rt') as fd:
    data = json.load(fd)  # напрямую из файла

for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {', '.join(value)}')
    else:
        print(f'{key}: {value}')

# прочитать как строку
with open('dogs.json', 'rt') as fd:
    temp = fd.read()  # читаем файл как строку
    data = json.loads(temp)  # строковое представление json

for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {', '.join(value)}')
    else:
        print(f'{key}: {value}')

for i in range(len(data)):
    print(f'\nПитомец №{i+1}')
    for k, v in data[i].items():
        if type(v) == list:
            print(f'\t{k}: {', '.join(v)}')
        else:
            print(f'\t{k}: {v}')

d = {
    'ананас': 300,
    'банан': 400,
    'яблоко': 120 ,
    'груша': 280
}

with open('fruits.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=4)  # записываем в файл

# вывод в виде строки
data = json.dumps(d, indent=4)
print(data)
