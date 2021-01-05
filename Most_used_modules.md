# Modules
Python的模块就像是工具包一样，如果要使用该工具包里的工具，就需要调用它。一般是用`import`或者`from...import`来实现调用。这个模块有的是Python自带e.g.`datatime`，有的是需要下载并安装e.g. `matplotlib`，而有的则可以自己来制作e.g. `add.py`。
```python
#我们定义了add这个函数是a+b，并保存为add.py，从而制作了自己的模块`add.py`。
def add(a,b):
    return a + b
```
**下面就是常用的模块及使用方法

## datetime(Python in-built)
**datetime模块是重新封装了time模块，有更丰富的接口：date,time,datetime,timedelta,tzinfo.

**1.datetime**

datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )
| 实参                                                      | 含义                           |
| ----------------------------------------------------------| ------------------------------ |
| %A                                                        | 星期的名字，比如Monday          |
| %B                                                        | 月份名，如January              |
| %m                                                        | 用数字表示月份                  |
| %d                                                        | 数字表示月份的某一天            |
| %Y                                                        | 四位的年份，如2018              |
| %y                                                        |两位的年份，如18                 |




```python
#将格式字符串转换为datetime对象。
datetime.strptime(date_string, format)
#根据date和time，创建一个datetime的对象。
datetime.combine(date, time)
```

**2.timedelta**

**3.tzinfo**



## CSV(Python in-built)
**CSV格式是纯文本存储的格式，一般用`with open('file path', 'r')`或者`with open('file path', 'r') as X`打开。**

```python
#返回一个读取器的对象
csv.reader()
#返回一个编写器的对象
csv.writer()
```


## Matplotlib and Numpy(Install)
**Matplotlib是Python的一个绘图库，可以在["官网下载"](<https://matplotlib.org/>)whl文件再安装，也可以点开一个Python终端，使用如下代码：**
```python
#我也不知道为什么此方法要安装几次才行，中途多次报错。Win系统还得安装visual studio才可以使用。
python -m pip install -U pip
python -m pip install -U matplotlib
```
```python
from matplotlib import pyplot as plt

plt.title("Supply of Apple")   #图表标题
plt.xlabel("Price")            #X轴名称
plt.ylabel("Quantity")         #y轴名称
plt.plot(x,y)                  #这里面还可以填很多参数，具体使用时再查
plt.show()                     #展示图表

plt.tick_params(axis,which,length,width,labelsize,labelcolor,etc.)
#tick_params的用法非常广泛，大体上是把图表做得更好，具体参数的含义如下：
"""
axis : {‘x’, ‘y’, ‘both’} Axis on which to operate; default is ‘both’. （axis:轴）
reset : bool If True, set all parameters to defaults before processing other keyword arguments. Default is False.
which : {‘major’, ‘minor’, ‘both’} Default is ‘major’; apply arguments to which ticks.
direction : {‘in’, ‘out’, ‘inout’} Puts ticks inside the axes, outside the axes, or both.
length : float Tick length in points.
width : float Tick width in points.
color : color Tick color; accepts any mpl color spec.
pad : float Distance in points between tick and label.
labelsize : float or str Tick label font size in points or as a string (e.g., ‘large’).
labelcolor : color Tick label color; mpl color spec.
colors : color Changes the tick color and the label color to the same value: mpl color spec.
zorder : float Tick and label zorder.
bottom, top, left, right : bool or {‘on’, ‘off’} controls whether to draw the respective ticks.
labelbottom, labeltop, labelleft, labelright : bool or {‘on’, ‘off’} controls whether to draw the respective tick labels.
labelrotation : float Tick label rotation
"""
```
