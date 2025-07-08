# Сериализация и Десериализация
# когда мы сложную структуру представляем последовательностью байтов и наоборот
# способ <пиклинг>
import pickle
import pprint

d = {
    'стол': 'table',
    'стул': 'chair'
}
# сериализация
with open('dictfile.da', 'wb') as p:
    # d - что сериализуем
    # p - куда сериализуем
    pickle.dump(d, p)

# десериализация
with open('dictfile.da', 'rb') as p:
    d = pickle.load(p)

pprint.pprint(d, width=15)