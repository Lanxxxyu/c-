import matplotlib.pyplot as pit
namelist=['mart','roy','jack','pp','cxk']
list=[0]*len(namelist)
for i in range(5):
    num=eval(input(f"请输入你要投票的对象(1-{len(namelist)}):"))
    list[num-1]=1+list[num-1]
pit.bar(namelist,list,0.2,color='blue')
pit.show()  