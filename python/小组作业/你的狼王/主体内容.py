import turtle as t
from random import randint
import grassland
import moon
import star
import windmill
import tree
import p
t.pencolor("yellow")
for k in range(50):
    x=randint(-200,400)
    y=randint(300,400)
    l=randint(15,20)
    star.star(x,y,l)
t.screensize(400.400,)
moon.moon(60)
grassland.caodi(-700,-220,2000,200)
windmill.windmill(300,-170,80)
tree.tree(-240,-40)
tree.tree(-120,-40)
tree.tree(0,-40)
p.setting()           #画布、画笔设置
x=0
p.nose(-100,100+x)      #鼻子
p.head(-69,167+x)       #头
p.ears(0,160+x)         #耳朵
p.eyes(0,140+x)         #眼睛
p.mouth(-20,30+x)       #嘴
p.cheek(80,10+x)        #腮
p.body(-32,-8+x)        #身体
p.hands(-56,-45+x)      #手
p.foot(2,-177+x)        #脚          
t.done()