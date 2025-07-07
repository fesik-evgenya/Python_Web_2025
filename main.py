# Файлы и ОС-модули
# позволяет создавать различные библиотеки, файлы и т.п.

import os

# будет создана директория в корневом каталоге
os.mkdir('libs')

# Мягкое создание директории ( вместо mkdir)
os.makedirs('libs', exist_ok=True)

# удаление директории
os.rmdir('libs')

# проверка существования пути
os.path.exists('libs')

# get current working directory
path = os.getcwd()
print(path)

# выйти на нужную директорию
os.chdir(path + '/images')

# выскочить на уровень выше и занырнуть в другую директорию
os.chdir('..')
os.chdir(path + '/fonts')
print(os.getcwd())

# получить список всех файлов в директории по условию
all_files = [f for f in os.listdir('.') if f.endswith('.ttf')]
os.chdir('..')
print(all_files)
