# Вывести фразу из потока, с наименьшим количеством слов в ней,
# все слова через пробел
import sys

data = [d.strip('\n') for d in sys.stdin.readlines()]

temp = [] # индекс строки в data и число слов в виде кортежей
for i, s in enumerate(data):
    temp.append((i, len(s.split())))

temp.sort(key=lambda x:x[1])
index = temp[0][0]
res = sorted(data[index].split())
print(*res, sep='-')

# Рекурсия - возможна только в функции
# Это такая функция, которая вызывает сама себя
#
# =
def factorial(count: int) -> int:
    result = 1
    for i in range(2, count + 1):
        result *= i
    return result
for x in range(10):
    print(x, factorial(x))

def factorial_rec(x: int) -> int:
    if x == 1 or x == 0:  # базовый вариант
        return 1  # базовый вариант
    return x * factorial_rec(x - 1)  # рекурсивная "пружина"

print( factorial_rec(10))

# Черепашья графика
import turtle as t

def square(side: int) -> None:
    for _ in range(4):
        t.forward(side)
        t.right(90)


def flower(n: int, circle: int) -> None:
    for _ in range(n):
        t.circle(circle)
        t.right(360 // n)

N = 5
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

t.bgcolor('black')
angle = 360 // len(colors) -1

for x in range(200):
    t.pencolor(colors[x % len(colors)])
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(angle)

flower(15, 20)

t.speed(10)
t.penup()
t.goto((-300),300)
t.pendown()

flower(15, 20)

t.penup()
t.goto(0,0)
t.pendown()

for _ in range(N):
    t.circle(50)
    t.right(360 // N)

t.penup()
t.goto(300,-250)
t.pendown()

for _ in range(N):
    square(100)
    t.right(360 // N)

#t.mainloop()
# Фрактал - математическая структура, где какая-то фигура повторяется,
# но с учётом масштаба, с рекурсией
# фрактальное дерево
def tree(length):
    if length < 10:
        return
    t.forward(length)
    t.left(30)
    tree(length * 0.7)
    t.right(60)
    tree(length * 0.7)
    t.left(30)
    t.backward(length)


t.left(90)
tree(100)
t.mainloop()