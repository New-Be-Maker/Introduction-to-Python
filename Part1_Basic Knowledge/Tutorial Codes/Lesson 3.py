# coding=gbk
'''����ѧϰ�б�'''

'''3.1�����о�ѭ���б�'''
#�������δ������ƶ���һ�����б���Ȼ������һ����ѭ�����������ʾ�������ѭ����
magicians = ['alice','david','carl']
for magician in magicians:
	print(magician)

'''for XXX in XXX���߼����ǣ�Python�ȶ���line7����line6��line7����Python����
��magicians�����ÿһ��Ԫ�ض�ѭ��һ�Σ����洢��magician���������'''

for magican in magicians:
	print(magician.title()+",that was a great trick!")
	print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone, that was a magic night!")
#������δ���ǳ���Ҫ��һ�����print�����������Ϊ������print�Ż���for xxx in xxx��ѭ��
#���к���Ҫ��һ�㣬����һ��Ҫ�������ð�ţ�����Python��һ��Ҫ��ʼ������
#����ע������P46-P49
print("\n\n\n\n\n\n\n")

'''3.2���������б�###
ѧ��ʹ��range()�����������'''

for value in range(1,8):
	print(value)
#�����ܷ���ֻ��7�����֣�����Ǳ�������в�һ�еĽ����
#�߼���ָ���ĵ�һ��ֵ��ʼ��������ָ���ĵڶ���ֵֹͣ����������

numbers = list(range(1,6))
print(numbers)
even_numbers = list(range(2,11,2))
print(even_numbers)

print("\n\n\n\n\n\n\n")

#������η��Ĳ�����������֮ǰѧ�ļ�������
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)
#�������ǽ���һ���յ��б�squares",Ȼ�����á�range�����������Python��1-10��������������
#Ȼ����ѭ��������������˷������ѳ˷�֮������֣����á�append���ķ����ٷŻؿ��б��С�
'''!!!�����Ĵ������ǲ�����square����м���'''
for value in range(1,12):
	squares.append(value**2)
print(squares)
#ע��Ŷ��������ʾ�������б��Ǽӵ�[]������б��еģ���������
'''!!!��������Ĵ���'''
cubes = [value**3 for value in range(1,5)]
print(cubes)
#ֱ���ڿ��б���д���뼴��

print("\n\n\n\n�б����Ƭ")

'''3.3�б����Ƭ###
���������Ҫ��һ���б��������Ҫ����ʹ��ĳ����Ԫ�أ�����δ���'''

players = ['tom','martina','michael','eric','eli']
print(players[0:3])
#�������ϵĴ������ֻѡ����ǰ��3���˶�Ա�����ˡ���Ƭ����[0:3]�ĺ����ǣ���0��ʼ������3����ʵ���ǵ��ĸ��ˣ�����������������3������
#����������������ڸ�����Ƭ��ѡ��
print(players[2:])
#�����ʾ���Ǵӵ�2����ʼ��ʵ���ǵ�3���ˣ���֮������С�
print(players[-3:])
#������ʾ����3������

'''���ۺ�����һ��������'''
print("\n\n\n\n")

print("Here are my first three players on my team")
for player in players[0:3]:
	print (player.title())

'''3.4�����б�###
�������ƵĻ�ֱ�ӿ�����[:]����ѡ��ĸ��ƵĻ�����Ƭ�����Ҫ�����Ӽ�Ԫ�صĻ�����append�ȡ�'''

my_foods = ['pizza','falafel','cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('salad')

print("my favorite foods are:")
print(my_foods)

print("my friend's favorite foods are:")
print(friend_foods)

#���ϵ����ӽ���������Ӷ����ˡ�

print("\n\n\n\n")
'''3.5Ԫ��###
�ڳ����У��б��ǿ��Ը��ĵģ���������ҪһЩ���ɸ��ĵĶ������������Ԫ��
��Ԫ����б�ͬ����Ԫ���õ���()������[]��'''

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions[0] = 250
#����������ǻᷢ��Python������ΪԪ���Ԫ���ǲ��ܱ��޸ĵġ�

'''Ԫ���Ԫ�ز��ɸ��ģ�������ζ��Ԫ�鲻�ܸ��ġ�'''

dimensions = (300,100)
for dimension in dimensions:
	print(dimension)
#���Ｔ�ɿ������µ�dimensions��Ԫ�鱻�޸��ˡ�




