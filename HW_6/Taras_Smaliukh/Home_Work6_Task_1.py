def you_max_num(a, b):
	
	""" Function that returns the largest number of two numbers """

	if a >= b:
		return a
	else:
		return b

print("Enter two numbers")

a = int(input("'a' will be :   "))
b = int(input("'b' will be :   "))

print(' The largest number is : ', you_max_num(a, b))