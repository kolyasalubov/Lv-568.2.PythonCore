from math import pi
from math import pow



def rectangle_square(a, b):

	"""Function that calculates the square of ​​a rectangle"""

	return float(a*b)

def triangle_square(a, b, c):

	"""Function that calculates the square of ​​a triangle"""

	return float(((a+b+c) * (b+c-a) * (a+c-b) * (a+b-c))**0.5) / 4

def circle_square(r):

	"""Function that calculates the square of ​​a circle"""

	# Pi = 3.14

	return float(pi * pow(r, 2))
