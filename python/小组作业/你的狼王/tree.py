import turtle as t
def tree(x,y):
    t.up()
    t.goto(x-144,y-177)
    t.down()
    t.color("#473005")
    t.pensize(20)
    t.goto(x-144,y-80)
    t.color("#009900")
    t.dot(50)#绘制一个指定直径和颜色的圆点
    t.goto(x-114,y-80)
    t.dot(50)
    t.goto(x-174,y-80)
    t.dot(50)
    t.goto(x-124,y-50)
    t.dot(40)
    t.goto(x-164,y-50)
    t.dot(40)
    t.goto(x-144,y-25)
    t.dot(40)
    t.end_fill()
