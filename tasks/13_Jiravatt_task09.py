import turtle

__Pen = turtle.Pen()

time_step = 0.1
scale_factor = 1
x = -400

turtle.setup(width=800,height=600,startx=200,starty=300)
__Pen.penup()
__Pen.goto(-400, 0)
speed = turtle.numinput('Speed simulator','What speed do you want?',1.0)
# A line below makes a conversion to 'Block' view possible
speed = float(speed)

while x < 400:
    __Pen.forward(time_step * speed * scale_factor)
    x += time_step * speed * scale_factor

# turtle.done()
