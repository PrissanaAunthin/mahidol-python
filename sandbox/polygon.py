import turtle
import time

__Pen = turtle.Pen()


List = input('How many sides do you want?')
dtheta = 0
__Pen.left(90)
for index in range(0,numside):
    __Pen.forward(100)
    __Pen.right(90)
    time.sleep(1)
turtle.done()
