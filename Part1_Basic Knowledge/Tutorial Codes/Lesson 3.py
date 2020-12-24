# coding=gbk
'''深入学习列表'''

'''3.1深入研究循环列表'''
#下面的这段代码先制定了一个“列表”，然后定义了一个“循环”，最后显示了这个“循环”
magicians = ['alice','david','carl']
for magician in magicians:
	print(magician)

'''for XXX in XXX的逻辑就是，Python先读了line7而非line6，line7告诉Python的是
把magicians里面的每一个元素都循环一次，并存储到magician这个变量里'''

for magican in magicians:
	print(magician.title()+",that was a great trick!")
	print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone, that was a magic night!")
#上面这段代码非常重要的一点就是print的缩进与否，因为缩进的print才会有for xxx in xxx的循环
#还有很重要的一点，就是一定要在语句后加冒号，告诉Python下一行要开始缩进。
#其他注意事项P46-P49
print("\n\n\n\n\n\n\n")

'''3.2创建数字列表###
学会使用range()函数与简单运算'''

for value in range(1,8):
	print(value)
#这里能发现只有7个数字，这就是编程语言中差一行的结果。
#逻辑：指定的第一个值开始数，到达指定的第二个值停止（不含）。

numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n\n\n\n\n\n\n")

#这个二次方的操作，集合了之前学的几个代码
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
#首先我们建立一个空的列表“squares",然后利用”range“这个方法让Python把1-10的数都数出来。
#然后用循环把里面的数都乘方，最后把乘方之后的数字，都用“append”的方法再放回空列表中。
'''!!!更简洁的代码则是不利用square这个中间商'''
for value in range(1,12):
	squares.append(value**2)
print(squares)
#注意哦，这里显示出来的列表都是加到[]这个空列表中的，加了两次
'''!!!最最最简洁的代码'''
cubes = [value**3 for value in range(1,5)]
print(cubes)
#直接在空列表里写代码即可

print("\n\n\n\n列表的切片")

'''3.3列表的切片###
这个部分主要讲一下列表中如果想要单独使用某几个元素，该如何处理'''

players = ['tom','martina','michael','eric','eli']
print(players[0:3])
#比如以上的代码就是只选择了前面3个运动员进行了“切片”，[0:3]的含义是，从0开始，到第3个（实际是第四个了）结束结束（不含第3个）。
#这个方法可以适用于各种切片节选。
print(players[2:])
#这个表示的是从第2个开始（实际是第3个了），之后的所有。
print(players[-3:])
#这个则表示最后的3个！！

'''来综合运用一波！！！'''
print("\n\n\n\n")

print("Here are my first three players on my team")
for player in players[0:3]:
	print (player.title())

'''3.4复制列表###
完整复制的话直接可以用[:]，有选择的复制的话就切片，如果要单独加减元素的换，用append等。'''

my_foods = ['pizza','falafel','cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('salad')

print("my favorite foods are:")
print(my_foods)

print("my friend's favorite foods are:")
print(friend_foods)

#以上的例子将复制与添加都讲了。

print("\n\n\n\n")
'''3.5元组###
在程序中，列表是可以更改的，而我们需要一些不可更改的东西，这个就是元组
而元组和列表不同的是元组用的是()，而非[]。'''

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250
#这个代码我们会发现Python报错，因为元组的元素是不能被修改的。

'''元组的元素不可更改，但不意味着元组不能更改。'''

dimensions = (300,100)
for dimension in dimensions:
	print(dimension)
#这里即可看到，新的dimensions的元组被修改了。




