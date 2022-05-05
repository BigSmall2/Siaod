import math
import turtle
import time

#Кривая Серпинского
turtle.speed('fastest')

def halfSierpinski(size, level):
    if level == 0:
        turtle.forward(size)   # Вперёд
        return
    halfSierpinski(size, level - 1)
    turtle.left(45)
    turtle.forward(size * math.sqrt(2))
    turtle.left(45)             #поворачиваем черепаху
    halfSierpinski(size, level - 1)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    halfSierpinski(size, level - 1)
    turtle.left(45)
    turtle.forward(size * math.sqrt(2))
    turtle.left(45)
    halfSierpinski(size, level - 1)

def sierpinski(size, level):
    halfSierpinski(size, level)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    halfSierpinski(size, level)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

tic = time.time()
sierpinski(15, 3)
tac = time.time()
print(f"Построение кривой Серпинского заняло {tac - tic} секунд")
# serp(size, n)
turtle.done()

