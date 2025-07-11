# # Протоколы
#
# # Transmission Control Protocol (TCP) — протокол управления передачей
# # Internet Protocol (IP) - разбивает на пакеты (IP-дейтаграммы)
# # TCP/IP
# # HTTP(S) - Hyper Text Transfer Protocol (Secured)
# # FTP - File Transfer Protocol
# # SMTP - Simple Mail Transfer Protocol
# # Хост-система
# # 1. Обязательная - IP-адрес: 195.34.32.11
# # 2. Необязательная - DNS (Domain Name System)
# # http(s)://www.yandex.рф//
# # ASCII %20, %2C
# # URL - Uniform Resource Locator
# # http(s)://домен.зона/page1/?param1=value1&param2=value2
# # ../font/
#
# import sys
#
# print('Я', sys.argv[0], 'и мой аргумент', sys.argv[1])
#
#
# if len(sys.argv) >= 2:
#     match sys.argv[1]:
#         case 'p':
#             print('Привет')
#         case 'g':
#             print('Привет')
#         case _:
#             print('Не понял')

# Периодические задачи
import schedule
import datetime

i = 1
def job():
    global i
    print(f'Скрипт запустился {i}')
    i += 1
    t = datetime.datetime.now()
    print('Время: ', t.strftime('%H:%M:%S'))

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()