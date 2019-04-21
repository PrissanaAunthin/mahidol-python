import turtle
import math

__Pen = turtle.Pen()


def gcd(a,b):
    if (a < b):
        temp = a
        a = b
        b = temp
    while (b > 0):
        temp = b
        b = (a % b)
        a = temp
    return a

__Pen.speed(30)
numsides = int(turtle.numinput('Star Generator','How many points do you need?',5))
k = math.floor(numsides / 2)
while (gcd(numsides, k) > 1):
    k = (k - 1)
rotate_angle = (180 * ((2 * k) / numsides))
print(k)
print(rotate_angle)
for __count in range(numsides):
    __Pen.forward(150)
    __Pen.right(rotate_angle)
turtle.done()
