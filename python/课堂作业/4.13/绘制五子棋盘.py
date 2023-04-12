import turtle
def upto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
turtle.screensize(400,400)
for k in range (11):
    x1=-200
    y1=-200+40*k
    upto(x1,y1)
    turtle.goto(x1+400,y1)
for k in range (11):
    x1=-200+40*k
    y1=200
    upto(x1,y1)
    turtle.goto(x1,y1-400)
turtle.done()