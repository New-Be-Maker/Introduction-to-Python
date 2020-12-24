'''可以随时修改变量的值，但是Python只会记录最新的变量的值'''
'''e.g. I define twice "message", it is printed twice but "message"  is "XXX Crash" eventually'''


message = "Hello Python world"
print(message)

message = "Hello Python Crash Course world"
print(message)




'''变量命名原则###			
1.只能是字母、数字、下划线。数字不能打头。e.g. "name_1" not "1_name"。
2.没有空格。 e.g. "first_name" not "first name"
3.不要用函数名来作为变量名字。
4.慎用小写字母l和大写字母O。'''


'''1.1字符串的大小写更改###
e.g. The machanism of the following codes
title相当于是一个”方法“，而后面的括号是对于”方法“的进一步补充，这个地方不需要补充，所以就空着即可。
而”abc“是我们定义的变量，我们需要对”abc“施加”title"的“方法”。最后再使之显现出来，就有了print(abc.title())
后面的几段codes是将所有的字母改大小写，原理是一样的'''

abc = "ada lovelace"
print(abc.title())
#title:首字母大写
print(abc.upper())
#upper:大写
print(abc.lower())
#lower:小写


'''1.2合并字符串###
看codes就明白了,这个code的关键就是前后都有+"的出现'''

first_name = "Yifeng"
last_name = "Luo"
full_name = first_name +" "+ last_name
print(full_name)


'''1.3合并字符串以及设置变量的合并应用###
看codes就明白了，鉴于我们已经有fisrt_name，last_name，full_name了，我不再创建新变量
这里我们将创建新变量，合并字符串与变量都进行了综合应用'''

message_1 = "Hello," + full_name.upper() + "!"
print(message_1)


'''1.4字符串的换行以及添加空白###
如果要添加制表符，可以用"\t字符串“实现，如果要换行的话，用”\n“实现，同时运用的话，”\n\t“'''

print("\tPython")
print("Python\ngood\njob")
print("Python\n\tgood\n\tjob")


'''1.5删除字符串中的空白###
这个之所以重要是因为程序来讲，只认死理，有空白和无空白是不同的两个东西
比如下面的代码，'python ' 这个字符串显示出来其实只有python，但其实和'python'是两个事物
同时注意：用retrip这个代码消除了右边的空白后，只有当再次定义favorite_language后才会真正消除，要不然只是消除一次
strip,lstrip,rstrip 分别是全，左，右'''

favirite_language = 'python ' 
favirite_language.rstrip()
favirite_language = favirite_language.rstrip()


'''1.6数字###
Python中的数字就是 加(+)减(-)乘(*)除(/)乘方(**)'''
print(1+1)

'''1.7使用函数str()避免一些类型错误###
比如你想给某人生日快乐，写了这样的代码
age = 22
message = "happy" + age + "rd birthday!"
print(message)
但是Python会报错，因为Python这个时候不知道22到底是啥意思了，可能是字符22，也可能是一个数值22。'''

age = 33
message_2 = "happy " + str(age) + "rd birthday"
print(message_2)
#注意。"#"是用来编写注释的。上面那个地方注意happy后面是有个空格的，要不然happy就和33连起来了。

