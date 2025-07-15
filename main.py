# Погода через API
import requests
from PIL import Image
import io

API_KEY = 'c747bf84924be997ff13ac5034fa3f86'
URL = 'http://api.openweathermap.org/data/2.5/weather'
CITY = 'Санкт-Петербург'

params = {
    'q': CITY,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(URL, params=params)
result = response.json()
# print(result)

weather = result['weather'][0]['description']
temperature = result['main']['temp']
humidity = result['main']['humidity']
wind = result['wind']['speed']
data = result['coord']
ll = f'{data['lon']},{data['lat']}'
# print(ll)


print(f'Сегодня в городе {CITY}: {weather}')
print(f'Температура: {temperature:.1f}\xB0C')
print(f'Влажность: {humidity}%')
print(f'Скорость ветра: {wind} м/с')
link = f'https://static-maps.yandex.ru/1.x/?ll={ll}&spn=0.005,0.005&l=sat&pt={ll},pm2dgl'
image = requests.get(link).content
if image:
    im = Image.open(io.BytesIO(image)).convert('RGB')
    im.save('map.jpg')


