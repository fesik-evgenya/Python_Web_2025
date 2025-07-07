# # Пишем и подключаем свои модули
# # from . lib import summ - из текущей директории
# # from .. lib import summ - уровнем выше
# # from .lib import summ - относительный импорт
# from lib import summ
#
#
# def main():
#     print(summ(7, 3))
#
#
# if __name__ == '__main__':
#     main()
from traceback import print_tb

from package1 import *  # для __all__
print(greet('Мир!'))  # тянет из модуля из пакета
print(sum_num(5,1))
