def square_of_a_rectangle(first_side_of_the_rectangle, second_side_of_the_rectangle):
	"""Function that calculates the square of ​​a rectangle."""

	return first_side_of_the_rectangle * second_side_of_the_rectangle


def square_of_a_triangle(first_side_of_the_triangle, 
                        second_side_of_the_triangle, 
                        third_side_of_the_triangle):
	"""Function that calculates the square of ​​a triangle."""

	return ((first_side_of_the_triangle + third_side_of_the_triangle - second_side_of_the_triangle)
             * (first_side_of_the_triangle + second_side_of_the_triangle - third_side_of_the_triangle)
             * (first_side_of_the_triangle + second_side_of_the_triangle + third_side_of_the_triangle)
             * (second_side_of_the_triangle + third_side_of_the_triangle - first_side_of_the_triangle)
            ) ** 0.5 / 4


def square_of_a_circle(radius_of_a_circle):
	"""Function that calculates the square of ​​a circle."""

	NUMBER_PI = 3.14
	return NUMBER_PI * radius_of_a_circle**2


def message(text):
    """Print text."""
    
    print(text)


while True:
    the_entered_number_option = input(
        '\n'   + 'What you want to calculate?:'
        '\n\t' + 'Square of ​​a rectangle, enter number: "1"'
        '\n\t' + 'Square of triangle, enter number: "2"'
        '\n\t' + 'Square of circle, enter number: "3"'
        '\n\t' + 'If you want exit, enter number: "0"'
        '\n\t' + 'Enter: '
        )

    if the_entered_number_option == "1":
        first_side_of_the_rectangle, second_side_of_the_rectangle = (
            float(input("Enter the size of the first side of the rectangle: ")),
            float(input("Enter the size of the second side of the rectangle: "))
            )
        calculation_result = square_of_a_rectangle(
            first_side_of_the_rectangle, 
            second_side_of_the_rectangle
            )
        calculation_result = "Square of ​​a rectangle: " + str(calculation_result)

    elif the_entered_number_option == "2":
        first_side_of_the_triangle, second_side_of_the_triangle, third_side_of_the_triangle = (
            float(input("Enter the size of the first side of the triangle: ")),
            float(input("Enter the size of the second side of the triangle: ")),
            float(input("Enter the size of the third side of the triangle: "))
            )
        calculation_result = square_of_a_triangle(
            first_side_of_the_triangle, 
            second_side_of_the_triangle, 
            third_side_of_the_triangle
            )
        calculation_result = "Square of ​​a triangle: " + str(calculation_result)

    elif the_entered_number_option == "3":
        radius_of_a_circle = float(input("Enter the radius of a circle: "))
        calculation_result = square_of_a_circle(radius_of_a_circle)
        calculation_result = "Square of ​​a circle: " + str(calculation_result)

    elif the_entered_number_option == "0":
        message("=======================\n" + "Exit.")
        break

    else:
        calculation_result = "=======================\n" + "Make your choice!"
    
    message(calculation_result)