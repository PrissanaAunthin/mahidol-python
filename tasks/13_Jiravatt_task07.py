import turtle
import random

__Pen = turtle.Pen()


__Pen.speed(10)
numsteps = int(turtle.numinput('Random Motion','How many steps do you need?'))
for __count in range(numsteps):
    __Pen.setheading(random.uniform(0, 359.9))
    __Pen.forward(30)
turtle.done()
