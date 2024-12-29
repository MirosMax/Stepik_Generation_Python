from turtle import Turtle

t = Turtle()

n = 12
t.shape('turtle')
t.stamp()
angle = 360 / n
t.pensize(5)
t.screen.colormode(255)
t.screen.bgcolor(173, 216, 230)
for _ in range(n):
    t.penup()
    t.fd(100)
    t.pendown()
    t.fd(15)
    t.penup()
    t.fd(15)
    t.stamp()
    t.penup()
    t.bk(130)
    t.left(angle)


t.screen.mainloop()