# coding=gbk
'''列表的学习'''
'''列表里的元素之间可以没有任何联系，用逗号隔开不同的元素
列表里面的元素是有顺序的，从0开始'''
#开始没法run，报错Non-UTF-8 code starting with '\xc1'，添加line1的备注后解决

computer = ['CPU','RAM','ROM']
print(computer[0].lower())
print(computer[-1].lower())
#-1是一个特殊语法，表示从最后一个，-2也可以表示倒数第二个



'''2.1修改/添加/插入/删除列表中的元素'''

motorcycles = ['honda','yamaha','suzuki']
#先定义一个列表，这里我们用摩托车
motorcycles[0] = 'ducati'
print(motorcycles)
#我们能从结果中看到，摩托车的列表中，'honda'没了，变成了'ducati'

motorcycles.append('lifan')
print(motorcycles)
#append这个‘方法’可以在列表中添加元素，但是注意，这个添加是直接添加到末尾。

motorcycles.insert(2,'BMW')
print(motorcycles)
#insert这个‘方法’可以在列表的具体位置中插入元素，上面的例子就是在插在第3个元素（2）的左边。

del motorcycles[2]
print(motorcycles)
#del就是删除某个元素的代码

'''！！！如果从列表中删除了某个元素，但是之后还想要用这个元素的话，不能用del！！！
要用pop这个代码，pop()会默认临时删除最后一个元素'''
#这里我们重新开始定义motorcycles
print('\nA new start' )
motorcyles = ['honda','yamaha','suzuki']
print(motorcycles)


#此处的疑问：为什么重新定义的motorcycles里面有lifan


poped_motorcyles = motorcycles.pop()
print(motorcycles)
print(poped_motorcyles)
'''如果知道具体的要删除的值，则用remove'''



'''2.2组织列表'''

cars = ['subaru','toyota','audi','bently']
cars.sort()
print(cars)
#sort这个‘方法’可以直接排序，不加其他条件的情况下，是按照首字母排序的，永久的
cars.sort(reverse=True)
print(cars)
#reserve=Ture是倒着排序，永久性的。
print(sorted(cars))
#sorted这个是临时排序，非永久。
cars.reverse()
print(cars)
#此处的reverse指的是排列的顺序，这里也可以看出，sorted只是一个临时的。

print('\n\n\n\nA new start')
print(len(cars))
