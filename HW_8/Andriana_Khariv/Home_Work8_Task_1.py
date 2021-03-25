class Polygon:
    def __init__(self, num_side):
        self.n = num_side
        self.side = [0 for i in range(num_side)]

    def inputsides(self):
        self.side = [float(input("Enter side " + str(i+1) + " : ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def square(self):
        a, b = self.side
        square = a * b
        print("The square of rectangle is ", str(square))

rec = Rectangle()
rec.inputsides()
rec.square()
