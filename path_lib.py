# здесь можно прописать все пути ко всем нужным директориям
from os import path

# __file__ - встроенная переменная
# содержащая путь к исполняемому скрипту

img_dir = path.join(path.dirname(__file__), 'images')
font_dir = path.join(path.dirname(__file__), 'font')
