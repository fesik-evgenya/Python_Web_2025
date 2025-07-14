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

# читаем через dict
with open('people.csv', 'r', encoding='utf-8') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(f'{row['name']} живёт в городе {row['city']}.')

field_names = ['name','age','city']
data = {
    'name': 'Борис',
    'age': '25',
    'city': 'Воронеж',
}

with open('file.csv', 'w', newline='', encoding='utf') as f:
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writerow(data)

# режим кватирования (сразу запись разных форматов в файл = строки-строками и числа-числами
data = ['name', 25 ,'town']
with open('sample.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(data)

# ZIP
from zipfile import ZipFile
import os

# заархиваровать
csv_files = [f for f in os.listdir() if f.endswith('.csv')]
with ZipFile('archive.zip', 'w') as myzip:
    for file in csv_files:
        myzip.write(file)
        os.remove(file)

# разархивировать
with ZipFile('archive.zip', 'r') as zip_obj:
    zip_obj.extractall()

# разархивировать конкретный файл
files_to_extract = ['people.csv', 'file.scv']
with ZipFile('archive.zip', 'r') as zip_obj:
    zip_obj.extractall(members=files_to_extract)

# список файлов в архиве
with ZipFile('archive.zip', 'r') as zip_obj:
    print(zip_obj.namelist())