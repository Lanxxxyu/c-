import turtle as t
def moon(x):
    t.bgcolor("#00BFFF")
    t.begin_fill()
    t.fillcolor("yellow")
    t.penup()
    t.pencolor("yellow")
    t.goto(-300,250)
    t.pendown
    t.circle(x)
    t.end_fill()