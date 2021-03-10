from task7_1 import *


i = int(input('Area of wich figure do you want to calculate? (Rectangle = 1, Triangle = 2 or Circle = 3) '))
if i == 1:
    square_rectangle(int(input('side of the rectangle a ')), int(input('side of the rectangle b ')))

elif i == 2:
    square_triangle(int(input('side of triangle h ')), int(input('side of triangle a ')))

elif i == 3:
    square_circle(int(input('radius of the circle ')))
else:
    print('the entered index is incorrect')

