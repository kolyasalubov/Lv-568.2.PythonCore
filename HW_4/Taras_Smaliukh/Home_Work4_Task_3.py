fibo_num = int(input("Enter your value :   "))

num1 = 0
num2 = 1
summ = 0
counter = 1

while counter <= fibo_num + 1:
	print(summ)
	num1 = num2
	num2 = summ
	summ = num1 + num2
	counter += 1


