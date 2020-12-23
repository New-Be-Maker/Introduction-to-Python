"""
E1.1 Input radius to calculate perimeter and area.
"""
#Suggested solution:

radius = float(input('please enter a radius:'))
perimeter = 2*3.14*radius
area = 3.14*radius*radius
print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area) 



"""
E1.2 Switch Fahrenheit to Celsius temperature.
"""
#Suggested solution:

f = float(input('plase enter Fahrenheit degree: '))
c = (f -32) / 1.8
print('%.1f Fahrenheit = %.1f Celsius' % (f,c))


"""
E2.1 Piecewise function calculation.

       2x + 12  (x > 1)
f(x) = 6x** - 1 (-1 <= x <= 1）
       9x + 2   (x < -1）
"""

#Suggested solution:

x = float(input('enter your x: '))

if x > 1:
    y = 2*x + 12
elif x >= -1:
    y = 6* x**2 - 1
else:
    y = 9*x +2
print('f(%f) = %.2f' % (x,y))


"""E2.2 Centenial system to level grade

grade => 90, A | 80 =< grade < 90, B | 70 =< grade < 80, C | grade < 70，D

"""

#Suggested solution：

grade = float(input("enter your score: "))
if grade => 90:
  grade = "A"
elif grade => 80:
  grade = "B"
elif grade => 70:
  grade = "C"
else:
  grade = "D"
print("Your grade level is: ", grade) 
