from random import randint
import turtle 
import ploygon
def star(x,y,l):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(l)
        turtle.rt(144)
    turtle.end_fill()
turtle.screensize(400,400,"yellow")
turtle.pencolor("black")
turtle.pensize(1)
turtle.speed(0)
for k in range(100):
    x=randint(-400,400)
    y=randint(-400,400)
    l=randint(15,20)
    star (x,y,l)
ploygon(x,y,)
turtle.done()