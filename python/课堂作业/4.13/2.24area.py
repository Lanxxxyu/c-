import math
def func(a,b,c):
    h=(a+b+c)/2
    s=math.sqrt(h*(h-a)*(h-b)*(h-c))
    return s
a=float(input("请输入a"))
b=float(input("请输入b"))
c=float(input("请输入c"))
print("三角形面积为:",func(a,b,c))