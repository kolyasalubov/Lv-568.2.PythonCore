def rectangle_square():
    """This function calculates the square of rectangle
    Input parameters: wight and height
    Input Parameters type - float, int
    Output return square of rectangle depends on input
    """
    width = float(input("Enter the wight of rectangle: "))
    height = float(input("Enter the height of rectangle: "))
    square = float(width*height)
    print("The square of rectangle: ", square)
rectangle_square()
print(rectangle_square.__doc__)