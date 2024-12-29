from turtle import *


r = 100
penup()
x, y = -(2 * r), 0
goto(x, y)
pendown()
pensize(7)
colors = ['blue', 'yellow', 'black', 'green', 'red']
shift_y = r * 1.2
for _ in range(5):
    pencolor(colors.pop(0))
    circle(radius=r)
    x += r
    y += shift_y
    y *= -1
    penup()
    goto(x, y)
    pendown()


mainloop()