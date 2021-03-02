class Polygon:
    def __init__ (self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        self.sides = [int(input(f'Enter side {str(i+1)} : ')) for i in range(self.number_of_sides)]

class Rectangle(Polygon):
    def __init__ (self):
        super().__init__(2)

    def calculateSquare (self):
        a, b = self.sides
        square = a * b
        print (f'Square is {square}')

Rectangle=Rectangle()
Rectangle.inputSides()
Rectangle.calculateSquare()