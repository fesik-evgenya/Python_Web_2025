# match - case (3.10>)

print('Возможные ходы:\n\tL - влево\n\tR - вправо\n\tF - прямо\n\tQ - выход')

while True:
    ch = input('Ваш выбор: ')
    match ch:
        case 'L' | 'l' | 'Л' | 'л':
            print('Свернули налево')
        case 'R' | 'r' | 'Р' | 'р':
            print('Свернули направо')
        case 'F' | 'f' | 'Ф' | 'ф':
            print('Пошли прямо')
        case 'Q' | 'q' | 'Й' | 'й':
            print('До свидания!')
            break
        case _: #gefault
            print('Выбор не ясен')
