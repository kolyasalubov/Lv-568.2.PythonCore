import math
PI = 3.14


def square_rectangle(a, b):
    print("square of rectangle = ", a * b)


def square_triangle(a, b, c):
    p = ((a + b + c) / 2)
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)


def square_circle(r):
    print(PI * (r**2))


i = int(input('Area of wich figure do you want to calculate? (Rectangle = 1, Triangle = 2 or Circle = 3) '))
if i == 1:
    square_rectangle(int(input('side of the rectangle a ')), int(input('side of the rectangle b ')))
elif i == 2:
    square_triangle(int(input('side of triangle a ')), int(input('side of triangle b ')), int(input('side of triangle c ')))
elif i == 3:
    square_circle(int(input('radius of the circle ')))
else:
    print('the entered index is incorrect')
