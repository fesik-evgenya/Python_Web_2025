# CSV-файлы
import csv

data = [
    ['name', 'age', 'city'],
    ['Борис', '25', 'Воронеж'],
    ['Ирина', '32', 'Тверь'],
    ['Владимир', '18', 'Санкт-Петербург'],
    ['Светлана', '27', 'Москва'],
]

# прочитали файл
with open('people.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)

# записали в файл
with open('employee.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
