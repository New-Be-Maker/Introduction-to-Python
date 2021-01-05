# Modules
Python的模块就像是工具包一样，如果要使用该工具包里的工具，就需要调用它。一般是用`import`或者`from...import`来实现调用。这个模块有的是Python自带e.g.`datatime`，有的是需要下载并安装e.g. `matplotlib`，而有的则可以自己来制作e.g. `add.py`。
```Python
#我们定义了add这个函数是a+b，并保存为add.py，从而制作了自己的模块`add.py`。
def add(a,b):
    return a + b
```
**下面就是常用的模块及使用方法

## datetime(Python in-built)
**datetime模块是重新封装了time模块，有更丰富的接口：date,time,datetime,timedelta,tzinfo.

**1.datetime**
datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )





