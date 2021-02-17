def num_max(num_1, num_2):
	
	""" Function returns the largest number of two numbers """

	if num_1 >= num_2:
		return num_1
	else:
		return num_2
num_1 = int(input("First number:    "))
num_2 = int(input("Second number:   "))
print(num_max(num_1, num_2), " is max number  ")