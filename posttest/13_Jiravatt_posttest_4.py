import turtle
import math

__Pen = turtle.Pen()
__Pen.speed(15)

# This code is generate from 'Block' view
__Pen.right(60)
__Pen.circle(150, steps=3)
__Pen.penup()
__Pen.goto((75 * math.sqrt(3)), (-75))
__Pen.setheading(0)
__Pen.pendown()
__Pen.circle(150, steps=3)
turtle.done()
