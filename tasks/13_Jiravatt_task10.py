import turtle

step_dist = 10
heading = 0

__Pen = turtle.Pen()

__Pen.speed(5)

while True:
    command = turtle.textinput('Draw by yourself!','Give me a command (up/down/left/right)')
    if command == 'up':
        heading = 90
    elif command == 'down':
        heading = -90
    elif command == 'left':
        heading = 180
    elif command == 'right':
        heading = 0
    else:
        break
    __Pen.setheading(heading)
    __Pen.forward(step_dist)

turtle.done()