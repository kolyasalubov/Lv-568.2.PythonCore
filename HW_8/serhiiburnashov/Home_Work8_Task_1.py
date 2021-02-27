class Polygon:
    """ Some text explaining the class. """

    def __init__(self, number_of_sides):
        """ Some text explaining the function. """

        self.number_of_sides = number_of_sides
        self.sides = [0 for item in range(number_of_sides)]

    def inputSides(self):
        """ Some text explaining the function. """

        self.sides = [float(input(f"Enter side {str(item + 1)}: ")) for item in
                      range(self.number_of_sides)]

    def displaySides(self):
        """ Some text explaining the function. """

        for item in range(self.number_of_sides):
            print(f"Side {item + 1} is {self.sides[item]}")


class Rectangle(Polygon):
    def __init__(self):
        """ Some text explaining the function. """

        super().__init__(2)

    def findArea(self):
        """ Some text explaining the function. """

        a, b = self.sides
        area = a * b
        print(f"Are of rectangle is: {area}")


rectangle = Rectangle()
rectangle.inputSides()
rectangle.displaySides()
rectangle.findArea()
