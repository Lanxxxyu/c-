import turtle
from math import *
turtle.screensize(400,400)
turtle.pencolor("pink")
r=100
for t in range(360):
    t=t/360*2*pi
    x=2*r*(sin(t)-1/2*sin(2*t))
    y=2*r*(cos(t)-1/2*cos(2*t))
    turtle.goto(x,y)
turtle.done()