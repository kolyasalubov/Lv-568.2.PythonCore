def rectangle(a,b):
    return a * b
def triangle(a,b,c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c))**(1/2)
    return round((s),2)
def circle(r):
    pi = 3.14
    return round((pi * r**2),2)
user = input("Please, type a square which you want to calculate, it could be 'rectangle', 'triangle' or 'circle': ")
while user.lower().strip() not in ["rectangle", "triangle", "circle"]:
    user = input("You have written incorrect data, please try again, it could be 'rectangle', 'triangle' or 'circle': ")
if user.lower().strip() == "rectangle":
    a, b = int(input("Type a first side length of the rectangle ")), int(input("Type a second side length of the rectangle "))
    print("The rectangle square is ", rectangle(a,b))
elif user.lower().strip() == "triangle":
    a,b,c = int(input("Type a first side length of the triangle ")), int(input("Type a second side length of the triangle ")), int(input("Type a third side length of the triangle "))
    print("The traingle square is ",triangle(a, b, c))
else:
    r = int(input("Type the radius of the circle "))
    print("The circle square is ", circle(r))