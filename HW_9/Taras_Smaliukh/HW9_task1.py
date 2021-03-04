
def youAge(age):
	return 'Odd' if age % 2 != 0 else 'Even'

try:
	age = int(input('Yuor age:  '))
	if age > 0:
		print(youAge(age))
	if age <= 0:
		print("Neagtive Error: You should entered a posirive number")

except ValueError as e:
	print("You should entered a number")

