#coding=gbk


def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	#定义了函数get_formatted_name，并”返回“了整洁的姓名。
	
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")print("dsafasd")
	l_name = input("Last name: ")
	
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")
	
		
	
	
