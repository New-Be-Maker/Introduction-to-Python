# coding=gbk
'''If����ʹ��'''

cars = ['audi','bmw','sabaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
print('\n\n\n\n')
#���������߼���������һ�µĺܶ�����ˡ�

'''4.1��������###
ÿ��if���ĺ��Ķ���һ��ֵΪTure����False�ı��ʽ�����ǳ�Ϊ�������ԡ�'''

car = 'bmw'
car == 'bmw'
print(car == 'bmw')
print(car == 'audi')
#���ǻῴ����������ķֱ���Ture��False��
print('\n\n\n')

requested_topping = 'mushroom'

if requested_topping != 'anchovies':
	print('hold the anchovies')
#"!="������ű�ʾ����ȡ�

answer = 99

if answer >= 10:
	print('That is not the correct answer, please try again!')

'''���������'''
print('\n\n\n')
age_0 = 22
age_1 = 19
print(age_0 >= 10 and age_1 <=1)
#and��ʾ����������Ҫͬʱ������

'''����ض�ֵ��/�����б���'''
banned_users = ['andrew','carolina','david']
user = 'maria'

if user not in banned_users:
	print(user.title() +",you can post a response if you wish.")



'''4.2if-elif-else������'''

age = 17
if age >= 18:
	print("you are old enough to vote!")
	print("have you registered to vote yet")

else:
	print("sorry,you are too young to vote.")
#��������Ľ�����ǿ�������Ϊ����age��17����С��18�ģ����������else������ݡ�

print("/n/n/n/n")

'''�����кܶ�����������ǿ���ʹ��if-elif-else'''
'''���磺Ʊ���Ǹ��������շѵġ���3��
1.4���������
2.4-18���շ�5Ԫ
3.18�����ϣ������շ�10Ԫ'''

age = 12

if age < 4:
	print("your admission cost is 0")
	
elif age <= 18:
	print("your admission cost is 5")

else:
	print("your admission cost is 10")

#�˴����ǿ���������Ϊ5����Ϊ12����4-18֮������䡣
'''������Ƕδ������ʹ�ø������ķ�ʽ����'''

age = 12

if age < 4:
	price = 0
	
elif age <= 18:
	price = 5

else:
	price = 10
	
print("your admission cost is " + str(price) + ".")

'''if-elif-else����ʺ���ִ��һ������飬���Ҫִ�ж������飬
һ��Ҫʹ��һϵ�е�if��䡣����������Ӿ��������ġ�

e.g.���������кܶ������������˿�����ѡһ�ֻ��߶��֡��򵥻���Ҫ���������
������ mushroom�� peperroni��cheese'''
print("\n\n\n")

requested_toppings = ['mushroom', 'cheese']

if 'mushroom' in requested_toppings:
	print("adding mushroom")
if 'peperroni' in requested_toppings:
	print("adding peperroni")
if 'cheese' in requested_toppings:
	print("adding cheese")

print("\nfinished making your pizza!")

#�����δ���ʹ��if-elif-else���д�Ļ����ڵ�һ�������У�mushroom�Ѿ�ͨ���˲��ԣ�
#��ô���Ծ�ֹͣ�ˣ�������������ֻ��mushroom����û��cheese��
#�ڱ���������棬�߼�����Ҫ��


print("\n\n\n")
'''4.3����б���if�����ۺ�ʹ��'''

available_toppings = ['mushroom','olives','green pepper',
'peperroni', 'pineapple','cheese']

requested_toppings = ['mushroom','frendch fries','cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("adding " + requested_topping + ".")
	else:
		print("sorry, we don't have " + requested_topping + ".")

print("\nfinished making your pizza!")
