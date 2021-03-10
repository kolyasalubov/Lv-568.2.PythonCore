class Polygon:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.no_of_sides)]
            
    def dispsides(self):
        for i in range(self.no_of_sides):
            print(f"Side {i+1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def find_area(self):
        a, b = self.sides
        square = a * b
        return f"Square of the rectangle is {square}"

r = Rectangle()

r.input_sides()
print(r.dispsides())
print(r.find_area())