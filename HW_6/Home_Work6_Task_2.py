def rectangle_square():
    """This function calculates the square of rectangle
    Input parameters: wight and height
    Input Parameters type - float, int
    Output return square of rectangle depends on input
    """
    width = float(input("Enter the wight of rectangle: "))
    height = float(input("Enter the height of rectangle: "))
    square = float(width*height)
    return ("The square of rectangle: {}".format(square))
# rectangle_square()
# print(rectangle_square.__doc__)

def circle_square():
    """This function calculates the square of circle
    Input parameters int, float
    Output return square of circle
    """
    r = float(input("Please enter the radius of your circle: "))
    Pi = 3.14
    square = (Pi * (r**2))
    return ("Here is square of your circle: {}".format(round(square)))

def triangle_square():
    """The function calculates square of triangle
    Input parameters type float, int
    Output square of triangle
    """
    a = float(input("Please, enter lenght of the first side: "))
    b = float(input("Please, enter lenght of the second side: "))
    c = float(input("Please, enter lenght of the third side: "))
    p = (a + b + c)/2
    square = ((p*(p-a)*(p-b)*(p-c))**0.5)
    return ("Square of your triangle is: {}".format(round(square, 2)))

# triangle_square()

def square():
    """The function ask user for figure and then calculates square
    """
    choice = input("Please input what figure square you want to calculate(rectangle, triangle, circle): ")
    if choice == "rectangle":
        print(rectangle_square())
    elif choice == "circle":
        print(circle_square())
    elif choice == "triangle":
        print(triangle_square())
    else:
        print("Please enter the correct option (rectangle, triangle, circle): ")

square()