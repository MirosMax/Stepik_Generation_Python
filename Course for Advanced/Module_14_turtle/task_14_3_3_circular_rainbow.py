from turtle import *
import random


def random_color_rgb():
    colors = ()
    for _ in range(3):
        colors += (random.randint(0, 255), )
    return colors


def color_circle():
    speed(0)
    hideturtle()
    r = 200
    for _ in range(10):
        shift = 20
        fillcolor(random_color_rgb())
        begin_fill()
        circle(r)
        end_fill()
        r -= shift
        penup()
        left(90)
        fd(shift)
        right(90)
        pendown()


colormode(255)
color_circle()

mainloop()