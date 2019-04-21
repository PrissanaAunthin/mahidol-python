# This code is generate from 'Code' view

import turtle

__Pen = turtle.Pen()
NUMCELLS_X = 4
NUMCELLS_Y = 4
CELLSIZE = 50

__Pen.speed(30)

# Draw vertical line to seperate cells in horizontal
for i in range(0, NUMCELLS_X+1):
    __Pen.goto(i * CELLSIZE, 0)
    __Pen.setheading(90)
    __Pen.down()
    __Pen.forward(CELLSIZE * NUMCELLS_Y)
    __Pen.up()

# Draw horizontal line to seperate cells in vertical
for i in range(0, NUMCELLS_Y+1):
    __Pen.goto(0, i * CELLSIZE)
    __Pen.setheading(0)
    __Pen.down()
    __Pen.forward(CELLSIZE * NUMCELLS_X)
    __Pen.up()

# Finish!
turtle.done()