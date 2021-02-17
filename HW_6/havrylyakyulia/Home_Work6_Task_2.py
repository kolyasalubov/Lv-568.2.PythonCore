""" This function calculates the square of ​​a rectangle """
def rectangle_square(a, b):
	return a*b
""" This function calculates the square of ​​a triangle """
def triangle_square(a, b):
	return 1/2*a*b
""" This function calculates the square of ​​a circle """
def circle_square(r):
	return 3.14 * r**2

calc = input("What do you want? rectangle,triangle,circle:")
if calc == "rectangle":
    a = int(input("Side a: "))
    b = int(input("Side b: "))
    print(rectangle_square(a, b))
elif calc == "triangle":
    a = int(input("Side a: "))
    b = int(input("Height b: "))
    print(triangle_square(a, b))
elif calc == "circle":
    r = int(input("Radius: "))
    print(circle_square(r))
else:
    print("Error") 