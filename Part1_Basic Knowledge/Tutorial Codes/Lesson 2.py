# coding=gbk
'''�б��ѧϰ'''
'''�б����Ԫ��֮�����û���κ���ϵ���ö��Ÿ�����ͬ��Ԫ��
�б������Ԫ������˳��ģ���0��ʼ'''
#��ʼû��run������Non-UTF-8 code starting with '\xc1'�����line1�ı�ע����

computer = ['CPU','RAM','ROM']
print(computer[0].lower())
print(computer[-1].lower())
#-1��һ�������﷨����ʾ�����һ����-2Ҳ���Ա�ʾ�����ڶ���



'''2.1�޸�/���/����/ɾ���б��е�Ԫ��'''

motorcycles = ['honda','yamaha','suzuki']
#�ȶ���һ���б�����������Ħ�г�
motorcycles[0] = 'ducati'
print(motorcycles)
#�����ܴӽ���п�����Ħ�г����б��У�'honda'û�ˣ������'ducati'

motorcycles.append('lifan')
print(motorcycles)
#append������������������б������Ԫ�أ�����ע�⣬��������ֱ����ӵ�ĩβ��

motorcycles.insert(2,'BMW')
print(motorcycles)
#insert������������������б�ľ���λ���в���Ԫ�أ���������Ӿ����ڲ��ڵ�3��Ԫ�أ�2������ߡ�

del motorcycles[2]
print(motorcycles)
#del����ɾ��ĳ��Ԫ�صĴ���

'''������������б���ɾ����ĳ��Ԫ�أ�����֮����Ҫ�����Ԫ�صĻ���������del������
Ҫ��pop������룬pop()��Ĭ����ʱɾ�����һ��Ԫ��'''
#�����������¿�ʼ����motorcycles
print('\nA new start' )
motorcyles = ['honda','yamaha','suzuki']
print(motorcycles)


#�˴������ʣ�Ϊʲô���¶����motorcycles������lifan


poped_motorcyles = motorcycles.pop()
print(motorcycles)
print(poped_motorcyles)
'''���֪�������Ҫɾ����ֵ������remove'''



'''2.2��֯�б�'''

cars = ['subaru','toyota','audi','bently']
cars.sort()
print(cars)
#sort���������������ֱ�����򣬲�����������������£��ǰ�������ĸ����ģ����õ�
cars.sort(reverse=True)
print(cars)
#reserve=Ture�ǵ������������Եġ�
print(sorted(cars))
#sorted�������ʱ���򣬷����á�
cars.reverse()
print(cars)
#�˴���reverseָ�������е�˳������Ҳ���Կ�����sortedֻ��һ����ʱ�ġ�

print('\n\n\n\nA new start')
print(len(cars))
