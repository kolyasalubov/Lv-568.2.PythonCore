class Polygon:
    def __init__ (self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.number_of_sides)]

class Rectangle(Polygon):
    def __init__ (self):
        super().__init__(2)

    def calculateArea (self):
        a, b = self.sides
        area = a * b
        print ("Are of rectangle is : ", area)

My_Rectangle=Rectangle()
My_Rectangle.inputSides()
My_Rectangle.calculateArea()

