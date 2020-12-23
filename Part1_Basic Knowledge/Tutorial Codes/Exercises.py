"""
E1.Input radius to calculate perimeter and area.
"""
#Suggested solution:

radius = float(input('please enter a radius:'))
perimeter = 2*3.14*radius
area = 3.14*radius*radius
print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area) 



"""
E2.Switch Fahrenheit to Celsius temperature.
"""
#Suggested solution:

f = float(input('plase enter Fahrenheit degree: '))
c = (f -32) / 1.8
print('%.1f Fahrenheit = %.1f Celsius' % (f,c))
