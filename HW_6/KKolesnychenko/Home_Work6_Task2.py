def square_calculate():
    """The program that calculates the square of ​​a rectangle, triangle and circle """
    choice=input("Enter the geometric shape you want to calculate(rectangle, triangle and circle) ")
    if choice=="rectangle":
        height=int(input("Enter the height of a rectangle: "))
        width=int(input("Enter the width of a rectangle: "))
        rectangle_calculate(height,width)
        pass
    elif choice=="triangle":
        side_a=int(input("Enter the side A of a triangle: "))
        side_b=int(input("Enter the side B of a triangle: "))
        side_c=int(input("Enter the side C of a triangle: "))
        triangle_calculate(side_a,side_b,side_c)
    else:
        radius=int(input("Enter the radius of a circle: "))
        circle_calculate(radius)

def rectangle_calculate(height, width):
    """The function that calculate the square of ​​a rectangle
    Args:
        height ([int]): height of the rectangle
        width ([int]): width of the rectangle
    """
    square_rectangle=height*width
    return print(f"Square = {square_rectangle}")

def triangle_calculate(side_a,side_b,side_c):
    """The function that calculate the square of ​​a triangle
    Args:
        side_a ([int]): width of side A
        side_b ([int]): width of side B
        side_c ([int]): width of side C
    """
    perimeter=(side_a+side_b+side_c)/2
    square_triangle=(perimeter*(perimeter-side_a)*(perimeter-side_b)*(perimeter-side_c))**(1/2)
    return print(f"Square = {square_triangle}")

def circle_calculate(radius):
    """The function that calculate the square of ​​a circle
    Args:
        radius ([int]): width of radius
    """
    Pnum=3.14
    square_circle=Pnum*radius**2
    return print(f"Square = {square_circle}")

square_calculate()