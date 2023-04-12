c=input()
if c[-1] in {"f","F"}:
    c=(eval(c[0:-1])-32)/1.8
    print("{:.2f}C".format(c))
elif c[-1] in {"C",'c'}:
    c=(eval(c[0:-1]))*1.8+32
    print("{:.2f}F".format(c))
else:
    print("输入格式错误")