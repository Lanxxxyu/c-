list=[]
while 1:
    print("""
    0.退出
    1.初始化列表
    2.增加数据
    3.删除数据
    4.修改数据
    5.查找
    6.排序
    """)
    c=eval(input("请输入你想要使用的功能"))
    if c==0:
        break
    if c==1:#初始化列表
        del list[0::1]
        print("列表已经清零")
    if c==2:#增加数据
        print(list)
        x=eval(input("请输入你要添加的数据"))
        d=eval(input("请选择你需要增加数据的位置"))
        list.insert(d,x)
    if c==3:#删除数据
        print(list)
        d=eval(input("请选择你需要删除数据的位置"))
        del list[d-1:d:1]
    if c==4:#修改数据
        print(list)
        x=eval(input("请输入你要修改的数据的位置"))
        d=eval(input("修改后的数值"))
        list[x-1]=d
    if c==5:#查找
        x=eval(input("请输入你要查找的数据"))
        print(list.index(x))      
    if c==6:#排序
        print(list)
        a=eval(input("请输入你需要排序的方式 升序1 降序2"))
        if a==1:
            list.sort()
            print(list)
        if a==2:
            list.sort()
            list.reverse()
            print(list)

