from turtle import Turtle

t = Turtle()

t.shape('turtle')
t.screen.colormode(255)
t.screen.bgcolor(144, 238, 144)
shift = 1
for _ in range(100):
    t.stamp()
    t.penup()
    t.right(20)
    t.fd(shift)
    shift += 2

t.screen.mainloop()