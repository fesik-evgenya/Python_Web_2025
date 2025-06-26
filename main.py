# Подбор по росту
# 150 < height < 180
# Число кандидатов
# Число, кто прошёл по критерию
# Среди прошедших min и max
total = 0
total_success = 0
total_UnSuccess = 0
min_height = float('inf')
man_height = float('-inf')

while (height := int(input('Введите рост: '))) != -1:
    if 150 <= height <= 180:
        total_success += 1
        if height < min_height:
            min_height = height
        elif height > man_height:
            man_height = height
    else:
        total_UnSuccess += 1
    total += 1

print(f"""\n~~Статистика по кандидатам~~\nВсего кандидатов: {total} человек(а);\nУспешно прошли по критерию: {total_success} \
человек(а)\nНе подошли: {total_UnSuccess} человек(а)\nМинимальный рост успешных кандидатов: {min_height} см\nМаксимальный рост\
 успешных кандидатов: {man_height} см""")