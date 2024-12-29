from turtle import *
import random


def random_color_rgb():
    colors = ()
    for _ in range(3):
        colors += (random.randint(0, 255), )
    return colors


def snowflakes(scale, x, y):
    segment = 10 * scale
    speed(10)
    penup()
    goto(x, y)
    pendown()
    pencolor(random_color_rgb())
    pensize(4)
    for _ in range(8):
        for _ in range(3):
            fd(segment)
            left(45)
            fd(segment)
            bk(segment)
            right(90)
            fd(segment)
            bk(segment)
            left(45)
        fd(segment)
        bk(segment * 4)
        left(45)


x, y = -300, 300
colormode(255)
bgcolor(145, 152, 231)
for _ in range(4):
    scale = random.randint(1, 5)
    snowflakes(scale, x, y)
    penup()
    fd(600)
    pendown()
    x, y = pos()
    right(90)
snowflakes(2, 0, 0)

mainloop()
