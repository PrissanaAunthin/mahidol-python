import turtle

__Pen = turtle.Pen()

step_dist = 10
heading = 0
exit_status = 0
__Pen.speed(5)

def draw_command(step_command):
    if (step_command == 'u') :
        heading = 90
    elif (step_command == 'd') :
        heading = (-90)
    elif (step_command == 'l') :
        heading = 180
    elif (step_command == 'r') :
        heading = 0
    else :
        return False
    __Pen.setheading(heading)
    __Pen.forward(step_dist)
    return True

while True:
    command = turtle.textinput('Draw by yourself!','Give me a series of command (u/d/l/r)')
    if len(command) < 1:
        break
    else:
        for i in range(0,len(command)):
            step_command = command[i]
            if draw_command(step_command):
                pass
            else:
                break
            

turtle.done()