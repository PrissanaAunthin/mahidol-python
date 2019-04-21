import turtle

__Pen = turtle.Pen()


__Pen.speed(1)
__Pen.penup()
__Pen.goto(0, (-100))
__Pen.pendown()
__Pen.circle(100)
__Pen.penup()
__Pen.goto(70.71, (-70.71))
__Pen.setheading(45)
__Pen.pendown()
__Pen.circle(100, steps=4)
turtle.done()
