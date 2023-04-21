import random
a=[]
for i in range(20):
    c=random.randint(1,10)
    a.insert(i-1,c)
print(a)
b=a[1::2]
c=a[0::2]
#l.sort() #从小到大排序输出
#l.reverse() #列表顺序的倒置，从大到小输出
print(b)
b.sort()
b.reverse()
print(b)
for i in range(10):
    c.insert(2*i-1,b[i-1])
print(c)