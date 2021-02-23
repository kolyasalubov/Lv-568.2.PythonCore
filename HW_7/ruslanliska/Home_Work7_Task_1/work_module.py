import square
def calculating_square():
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

calculating_square()