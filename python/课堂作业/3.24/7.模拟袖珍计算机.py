while 1:
    a=int(input("请输入第一个操作数："))
    c=input("请输入操作符号")
    b=int(input("请输入第二个操作数："))
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=='*':
        print(a*b)
    elif c=='/':
        if(b==0):
            print("报错 0不能做除数")
        else :
            print(a/b)
    elif c=='%':
        if(b==0):
            print("报错 0不能做求余数")
        else:
            print(a%b)
    else :
        print("输入的符号有误")
    d=int(input("是否继续运算: 请输入1继续 输入0结束"))
    if d==0:
        print("收到 结束运算")
        break
    else:
        print("继续运算")
    