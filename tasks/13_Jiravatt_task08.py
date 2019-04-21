import turtle
import random
from math import sqrt

__Pen = turtle.Pen()

__Pen.speed(10)

__Pen.penup()
__Pen.goto(0,-150)
__Pen.pendown()
__Pen.circle(150)
__Pen.penup()
__Pen.backward(150)
__Pen.setheading(-45)
__Pen.pendown()
__Pen.circle(150*sqrt(2),steps=4)

cnt_hit = 0
cnt_all = 0
for i in range(int(turtle.numinput('Monte-Carlo simulations', 'How many times do you want?', default=100))):
    cnt_all = cnt_all + 1
    x = random.uniform(-150.0, 150.0)
    y = random.uniform(-150.0, 150.0)
    if x**2 + y**2 <= 150.0**2:
        cnt_hit = cnt_hit + 1
    __Pen.penup()
    __Pen.goto(x, y)
    __Pen.dot(5)

print('Hit:', cnt_hit, 'from', cnt_all)
print('Hit/all =', float(cnt_hit / cnt_all))

turtle.done()