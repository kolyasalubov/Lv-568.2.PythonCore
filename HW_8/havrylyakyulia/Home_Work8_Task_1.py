class Polygon:
    def __init__(self, number_of_sides):
        self.n = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputsides(self):
        self.sides = [float(input("Enter side " + str(i+1) + " : ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def area(self):
        a, b = self.sides
        area = a*b
        print("The area of rectangle is " , str(area))

r = Rectangle()
r.inputsides()
r.area()