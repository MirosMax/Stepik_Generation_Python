from turtle import Turtle
import random

t = Turtle()

t.screen.colormode(255)
shift = 5
pensize = 1
for _ in range(100):
    t.right(45)
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    t.pencolor(r, g, b)
    t.pensize(pensize)
    t.fd(shift)
    shift += 2
    pensize += 0.15


t.screen.mainloop()