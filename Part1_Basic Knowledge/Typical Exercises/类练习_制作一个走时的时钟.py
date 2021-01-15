import time

import self as self


class Clock(object):
    """
    如果是Python3.X，那么括号里即便没有值，其默认也是object，
    在3.X版本里，其默认加载的有很多，比如__init__;__new__等。
    具体加载项，请见：https://www.icode9.com/content-1-341525.html
    """
    def __init__(self, hour=0, minute=0, second=0):
        """
        __init__是做初始值的方法，有关类与对象的详情，可以参见
        教程：introduction to object oriented programming
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second


        
        
    def run(self):
         """
         此处我们定义走时这个函数。此处可看出，当我们在定义一个Clock类时，
         初始值是时分秒，因为我们假定Clock这个类都会有这几个元素。而走时
         的规则却不一定，比如有一些特定的钟表，走时并不是严格按一秒走一次，
         因此这里没有用到__init__。仅仅定义我们想要的走时方式。
         """
         self.sec += 1
         if self.sec == 60:
             self.sec = 0
             self.min += 1
             if self.min == 60:
                 self.min = 0
                 self.hour += 1
                 if self.hour == 24:
                     self.hour = 0

    def show(self):
         """
         此处定义将以怎样的方式来显示时间
         """
         # 此处的0>2d涉及到format count等知识，貌似2d表示使用填充。暂时不是很懂。
         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建一个时钟的"对象",相当于是这个对象必须要有初始的时分秒，run和show按需调用。
clock = Clock(23, 59, 58)		 
while True:
    # 先显示初始的clock时间（相当于把实参传递过去）
    print(clock.show())
    # 休眠一秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    # 此处的疑问是这个是否准时？因为计算机在运行run这个代码时也需要时间，虽然很短？
    clock.run()


