#coding=gbk


def get_formatted_name(first_name, last_name):
	"""�������������"""
	full_name = first_name + ' ' + last_name
	return full_name.title()
	#�����˺���get_formatted_name���������ء��������������
	
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")print("dsafasd")
	l_name = input("Last name: ")
	
	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello, " + formatted_name + "!")
	
		
	
	
