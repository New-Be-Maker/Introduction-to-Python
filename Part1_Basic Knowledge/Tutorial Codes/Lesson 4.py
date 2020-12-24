# coding=gbk
'''If语句的使用'''

cars = ['audi','bmw','sabaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
print('\n\n\n\n')
#这个代码的逻辑涵盖了这一章的很多概念了。

'''4.1条件测试###
每条if语句的核心都是一个值为Ture或者False的表达式，我们称为条件测试。'''

car = 'bmw'
car == 'bmw'
print(car == 'bmw')
print(car == 'audi')
#我们会看到两次输出的分别是Ture和False。
print('\n\n\n')

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
	print('hold the anchovies')
#"!="这个符号表示不相等。

answer = 99

if answer >= 10:
	print('That is not the correct answer, please try again!')

'''检查多个条件'''
print('\n\n\n')
age_0 = 22
age_1 = 19
print(age_0 >= 10 and age_1 <=1)
#and表示这两个条件要同时成立。

'''检查特定值在/不在列表中'''
banned_users = ['andrew','carolina','david']
user = 'maria'

if user not in banned_users:
	print(user.title() +",you can post a response if you wish.")



'''4.2if-elif-else的运用'''

age = 17
if age >= 18:
	print("you are old enough to vote!")
	print("have you registered to vote yet")

else:
	print("sorry,you are too young to vote.")
#这里输出的结果我们看出，因为给的age是17，是小于18的，所以输出了else里的内容。

print("/n/n/n/n")

'''假如有很多的条件，我们可以使用if-elif-else'''
'''比如：票价是根据年龄收费的。有3档
1.4岁以下免费
2.4-18岁收费5元
3.18岁以上（含）收费10元'''

age = 12

if age < 4:
	print("your admission cost is 0")
	
elif age <= 18:
	print("your admission cost is 5")

else:
	print("your admission cost is 10")

#此处我们看到输出结果为5，因为12是在4-18之间的年龄。
'''上面的那段代码可以使用更精炼的方式呈现'''

age = 12

if age < 4:
	price = 0
	
elif age <= 18:
	price = 5

else:
	price = 10
	
print("your admission cost is " + str(price) + ".")

'''if-elif-else语句适合于执行一个代码块，如果要执行多个代码块，
一定要使用一系列的if语句。下面这个例子就是这样的。

e.g.披萨店里有很多种披萨，客人可以自选一种或者多种。打单机需要最后打出来。
比如有 mushroom， peperroni，cheese'''
print("\n\n\n")

requested_toppings = ['mushroom', 'cheese']

if 'mushroom' in requested_toppings:
	print("adding mushroom")
if 'peperroni' in requested_toppings:
	print("adding peperroni")
if 'cheese' in requested_toppings:
	print("adding cheese")

print("\nfinished making your pizza!")

#如果这段代码使用if-elif-else语句写的话，在第一个测试中，mushroom已经通过了测试，
#那么测试就停止了，最后输出的内容只有mushroom，而没有cheese。
#在编程语言里面，逻辑很重要！


print("\n\n\n")
'''4.3多个列表与if语句的综合使用'''

available_toppings = ['mushroom','olives','green pepper',
'peperroni', 'pineapple','cheese']

requested_toppings = ['mushroom','frendch fries','cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("adding " + requested_topping + ".")
	else:
		print("sorry, we don't have " + requested_topping + ".")

print("\nfinished making your pizza!")
