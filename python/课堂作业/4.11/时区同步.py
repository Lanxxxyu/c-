from turtle import *
from time import *

def my_fd(l):
    pu()
    fd(l)

def Line(i, size):
    my_fd(size * 1)
    pd() if i else pu()
    fd(size * 10)
    my_fd(size * 1)
    rt(90)

def Num(n, size):
    Line(True, size) if n in "2345689" else Line(False, size)
    Line(True, size) if n in "134567890" else Line(False, size)
    Line(True, size) if n in "2356890" else Line(False, size)
    Line(True, size) if n in "2680" else Line(False, size)
    lt(90)
    Line(True, size) if n in "4567890" else Line(False, size)
    Line(True, size) if n in "23567890" else Line(False, size)
    Line(True, size) if n in "12347890" else Line(False, size)
    lt(180)
    my_fd(size * 5)

def Str(s, size = 2):
    pencolor("red")
    for i in s:
        if i == "+":
            write("年", font = ("Arial", 18, "normal"))
            my_fd(size * 15)
            pencolor("orange")
        elif i == "-":
            write("月", font = ("Arial", 18, "normal"))
            my_fd(size * 15)
            pencolor("green")
        elif i == "*":
            write("日", font = ("Arial", 18, "normal"))
            my_fd(size * 15)
            pencolor("blue")
        elif i == "/":
            write(":", font = ("Arial", 18, "normal"))
            my_fd(size * 15)
            pencolor("purple")
        else:
            Num(i, size)

def main():
    setup(800, 400, 0, 0)
    hideturtle()
    speed(0)
    pensize(2)
    my_fd(-275)
    Str(strftime("%Y+%m-%d*%H/%M", gmtime()))
    done()

main()
