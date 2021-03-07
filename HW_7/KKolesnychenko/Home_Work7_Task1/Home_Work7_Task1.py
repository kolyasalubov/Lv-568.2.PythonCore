import math

def rectangle_calculate(height, width):
    """The function that calculate the square of ​​a rectangle
    Args:
        height ([int]): height of the rectangle
        width ([int]): width of the rectangle
    """
    square_rectangle=height*width
    return print(f"Square = {square_rectangle}")

def triangle_calculate(side_a,height):
    """The function that calculate the square of ​​a triangle
    Args:
        side_a ([int]): width of side A
        height ([int]): height of triangle
    """
    square_triangle=0.5*height*side_a
    return print(f"Square = {square_triangle}")

def circle_calculate(radius):
    """The function that calculate the square of ​​a circle
    Args:
        radius ([int]): width of radius
    """
    square_circle=math.pi*math.pow(radius,2)
    return print(f"Square = {square_circle}")