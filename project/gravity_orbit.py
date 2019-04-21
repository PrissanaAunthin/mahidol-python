import turtle
from math import cos, sin, sqrt, pi

mass_1 = 1000.0
mass_2 = 200.0
position = [50.0, 0.0]
velocity = [0.0, 2.5]
acceleration = [0.0, 0.0]
timestep = 0.05


def distance(x, y):
    return sqrt(x**2 + y**2)

def gravity(x, y):
    return (mass_1 * mass_2 / distance(x, y)**2)

def sine(x, y):
    return (y / distance(x, y))

def cosine(x, y):
    return (x / distance(x, y))

def tangent(x, y):
    return (y / x)

__Pen = turtle.Pen()

__Pen.speed(10)

# __Pen.penup()
__Pen.goto(position[0],position[1])
__Pen.pendown()

while True:
    x = position[0]
    y = position[1]
    force = gravity(x, y)
    acceleration[0] = force * cosine(-1.0*x, -1.0*y) / mass_2
    acceleration[1] = force * sine(-1.0*x, -1.0*y) / mass_2
    velocity[0] = velocity[0] + acceleration[0] * timestep
    velocity[1] = velocity[1] + acceleration[1] * timestep
    position[0] = x + velocity[0] * timestep
    position[1] = y + velocity[1] * timestep
    __Pen.goto(position[0], position[1])
    print(x, y, velocity[0], velocity[1], sqrt(velocity[0]**2+velocity[1]**2))
    
# turtle.done()