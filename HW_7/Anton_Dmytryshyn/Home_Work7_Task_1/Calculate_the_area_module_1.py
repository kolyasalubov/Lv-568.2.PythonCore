from math import pow
from math import pi


def square_of_rectangle (a,b):
    """
    Takes in two sides of rectangle, then calculates its area
    """
    print(a * b)

def square_of_triangle (h,a):
    """
    Takes in the height and one side of  triangle  then calculates its area
    """    
    print(0.5 * h * a)    

def square_of_circle (r):
    """Takes in radius of the circle , then calculates its area"""
    print(pi * pow(r,2))

