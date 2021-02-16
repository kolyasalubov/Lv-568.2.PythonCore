def rectangle_square(a, b):

	"""Function that calculates the square of ​​a rectangle"""

	return float(a*b)

def triangle_square(a, b, c):

	"""Function that calculates the square of ​​a triangle"""

	return float(((a+b+c) * (b+c-a) * (a+c-b) * (a+b-c))**0.5) / 4

def circle_square(r):

	"""Function that calculates the square of ​​a circle"""

	Pi = 3.14

	return float(Pi * r**2)


while True:
	your_choise = input("If you want to calculate:\n square of rectangle  enter '1'\n square of triangle enter '2'\n square of circle  square enter '3'\n see you next time 'q'\n")

	if your_choise == '1':
		a = float(input("Enter size 'a':    "))
		b = float(input("Enter size 'b':    "))
		print(rectangle_square(a, b))

	elif your_choise == '2':
		a = float(input("Enter size 'a':    "))
		b = float(input("Enter size 'b':    "))
		c = float(input("Enter size 'c':    "))
		print(triangle_square(a, b, c))

	elif your_choise == '3':
		a = float(input("Enter the radius:    "))
		print(circle_square(a))

	elif your_choise == 'q':
		print("See you")
		break
	else:
		print('Try again')
