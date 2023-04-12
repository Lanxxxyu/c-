from random import randint
import turtle
def ploygon(x,y,n,l):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for i in range(n):
        turtle.fd(l)
        turtle.rt(360/n)
    turtle.end_fill()   
turtle.screensize(400,400,"black")
turtle.pencolor("yellow")
turtle.pensize(1)
turtle.speed(0)