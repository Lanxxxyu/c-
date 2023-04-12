import turtle as t
from random import randint
def star(x,y,l,):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.fd(l)
        t.rt(144)
    t.end_fill()
