import turtle

__Pen = turtle.Pen()


num_x = 4
num_y = 4
size = 100
__Pen.speed(15)
for index in range(0,(num_y + 1)):
    __Pen.pendown()
    __Pen.forward((size * num_x))
    __Pen.penup()
    __Pen.goto(0, ((index + 1) * size))
__Pen.goto(0, 0)
__Pen.setheading(90)
for index in range(0,(num_x + 1)):
    __Pen.pendown()
    __Pen.forward((size * num_y))
    __Pen.penup()
    __Pen.goto(((index + 1) * size), 0)
turtle.done()
