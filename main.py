# https://regex101.com
import re
# 2-я 'н' может присутствовать, но не обязательно
pattern = r'стеклянн?ый'
test_string = 'стеклянный, стекляный, оловянный, серебрянный'

# жадный квантификатор (greedy quantifier)
pattern = r'<img.*>'
test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'

result = re.findall(pattern, test_string)
print(result)

# ленивый квантификатор (lazy, non-greedy quantifier)
pattern = r'<img.*?>'
test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'

result = re.findall(pattern, test_string)
print(result)

# только путь к картинке
pattern = r'<img[^>]+src="([^">]+)"'
test_string = 'Картинка <img src="bg.jpg"> в тексте</p>'

result = re.findall(pattern, test_string)
print(result)

# Захватить содержимое тега <p>
pattern = '<p>(.*?)</p>'
test_string= '<b>вот начало: </b><p>Содержимое</p><i>и т.д.</i>'

result = re.findall(pattern, test_string)
print(result)

# захват абзаца в теге с атрибутами
pattern = r'<p[^>]*>(.*)</p>'
test_string= '<b>Центрируем</b><p align="center">Содержимое</p>'
result = re.findall(pattern, test_string)
print(result)

# Убираем все знаки препинания
def remove_punctuation(input_str: str) -> str:
    """
    Методом sub() заменяем все найденные совпадения
    пустой строкой и возвращаем "очищенную"
    :param input_str: строка со знаками препинания
    :return: строку, очищенную от зн. препинания
    """
    return re.sub(r'[^\w\s]', '', input_str)

test_string = 'Язык Python, являясь интуитивно понятным, прост для изучения. Ну и PEP8.'
print(remove_punctuation(test_string))

# через split() и join()
pattern = r'[,.;:! ]'
# убираем все пробелы
test_string = ''.join('яблоко,  груша,  банан;  слива  !  абрикос  '.split(' '))

result = re.split(pattern, test_string)
print(result)

# через регулярное выражение
pattern = r'[,.;:!]'
test_string = '  яблоко,  груша,  банан;  слива  !  абрикос  '

result = sorted(x.strip() for x in re.split(pattern, test_string))
print(result)

# вытащить инфу с сайта ( например ссылки на изображения)
import requests
pattern = r'<img[^>]+src="([^">]+)"'
# сначала проверим
# text_string = '<img height="50" width="150" src="./images/sunny_day_2.jpg"><>'

html = requests.get('https://skillbox.ru').text
result = re.findall(pattern, html)
print(result)
# result = re.findall(pattern, text_string)
# print(result)