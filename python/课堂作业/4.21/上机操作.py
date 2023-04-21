a=[1,2,3]
a.extend([4,5])
#exend是将元素挨个添加进列表中而不是以整体的方式加入 
#append是将元素以整体打包加入到列表中去
print(a)
a.insert(2,10)
a.insert(3,11)
#insert只能添加整体 如果要添加一个以上的元素则需要多次添加
print(a)
del a[0:2]
#冒号之后表示步频
print(a)