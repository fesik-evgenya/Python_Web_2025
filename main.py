# return vs yield
# разница <yield> - функция возвращает значение и продолжает работать
# создаёт генератор

def generate_list():
    for i in range(5):
        yield i  # генератор (возвращает, но не завершает)


array = list(generate_list())
print(array)