def square_of_rectangle (a,b):
    """Takes in two sides of rectangle, then calculates its area"""
    print(a * b)

def square_of_triangle (a,b,c):
    """
    Takes in three sides of triangle, checks if such a triangle exists,
    if yes - calculates its area
    """
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2 # half of the perimeter 
        print((p*(p-a)*(p-b)*(p-c)) ** 0.5) # using Heron's formula
    else:
        print ("There is no such a triangle")

def square_of_circle (r):
    """Takes in radius of the circle , then calculates its area"""
    Pi = 3.14
    print(Pi * (r ** 2))

a = input("Area of wich figure do you want to calculate? (Rectangle, Triangle or Circle) ")
if a == "Rectangle":
    square_of_rectangle(int(input("First side: ")),int(input("Second side: ")))
elif a == "Triangle":
    square_of_triangle(int(input("First side: ")),int(input("Second side: ")),int(input("Third side: ")))
elif a == "Circle":
    square_of_circle(int(input("Radius of circle: ")))
else:
    print ("You have to choose between Rectangle, Triangle or Circle")