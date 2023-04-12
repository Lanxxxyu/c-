import turtle as t
from math import *
import time
t.tracer(0)
def windmill(a,b,a1):
    t.penup()
    t.goto(a,b)
    t.pendown()
    b1=a1*2**0.5
    b2=2*a1
    dark_color=["#267fb9","#f2b11b","#538a30","#ba62c1"]   # 深色列表
    light_color=["#2aaad1","#f3d727","#7fbc2b","#cc81d2"]  # 浅色列表
    t.rt(22)
    for i in range(4):
        t.color(dark_color[i])
        t.begin_fill()
        t.fd(a1)
        t.lt(90)
        t.fd(a1)
        t.lt(135)
        t.fd(b1)
        t.end_fill()
        t.rt(180)
        t.color(light_color[i])
        t.begin_fill()
        t.fd(b1)
        t.lt(90)
        t.fd(b1)
        t.lt(135)
        t.fd(b2)
        t.end_fill()
        ### 绘图结束，隐藏海龟
    #棍子绘制即风车杠 length与较大直角边有直接关系 即l=1.7*r width=2/15*b1