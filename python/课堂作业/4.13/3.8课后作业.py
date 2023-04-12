import turtle
from math import *
turtle.screensize(400,400)
r=20
turtle.speed(0)
turtle.pensize(1)
turtle.pencolor("red")
for t in range(360*):
    t=t/360*2*pi
    x=r*(pow(e,cos(t))-2*cos(4*t)+pow(sin(t)/12,5))*r*cos(t)
    y=r*(pow(e,cos(t))-2*cos(4*t)+pow(sin(t)/12,5))*r*sin(t)
    turtle.goto(x,y)
turtle.done()          
       