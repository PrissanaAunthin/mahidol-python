import turtle

__Pen = turtle.Pen()


__Pen.speed(15)
__Pen.circle(100, steps=3)
__Pen.penup()
__Pen.setheading(0)
#base = sqrt(3) * circum_radius
__Pen.goto(86.6025, 40)
__Pen.pendown()
__Pen.setheading(60)
__Pen.circle(100, steps=3)
turtle.done()
