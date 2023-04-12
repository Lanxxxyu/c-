#剪刀石头布 判断
a=input("请a出拳")
b=input("请b出拳")
if a=='剪刀'and b=='剪刀':
    print("这局是平局")  
if a=='剪刀'and b=='石头':
   print("哈哈 这局b赢了")
if a=='剪刀'and b=='布':
    print("哈哈 这局a赢了")
if a=='石头'and b=='石头':
    print("这局是平局")  
if a=='石头'and b=='布':
   print("哈哈 这局b赢了")
if a=='石头'and b=='剪刀':
    print("哈哈 这局a赢了")
if a=='布'and b=='布':
    print("这局是平局")  
if a=='布'and b=='剪刀':
   print("哈哈 这局b赢了")
if a=='布'and b=='石头':
    print("哈哈 这局a赢了")

#a=input("姓名 语文 数学 英语 总分")
#c=a.split(" ")
#print("{}同学2022学期,语文{},数学{},英语{}总分{}。".format(*c))

#from random import randint
#x=randint(1,40)
#print(x)
#while True:
#    guess=eval(input("请输入一个1-100的数字:"))
#    if guess==x:
#       print("猜对了")
#       break  
#    if guess>x:
#       print("猜大了")
#    if guess<x:
#       print("猜小了")

#format的用法 如果直接配对 后者可多不可少 否则会报错

#字符串本身是能改变的
#s=input("请输入一段文字")
#list=("东京热","日本")
#for item in list:
#  s=s.replace(item,"***") 
#print(s)

#a=input().upper().split(" ")
#for item in a:
  #print(item[0],end='')