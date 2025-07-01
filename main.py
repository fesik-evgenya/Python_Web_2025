# проверка ДЗ - через множества
# фраза: ну, я типа, короче? вообще: короче, не , понимаю этот язык!
from pyexpat.errors import messages

commas = (',', '!', '.', '?', '-', ':' )
stop_words = {'ну', 'я', 'типа', 'короче', 'не'}

message = input('Введите сообщение: ')

for z in commas:
    message = message.replace(z, '')

lst = message.split()

for a, b in enumerate(sorted(set(lst) - stop_words), 1):
    print(f'{a}. {b}')