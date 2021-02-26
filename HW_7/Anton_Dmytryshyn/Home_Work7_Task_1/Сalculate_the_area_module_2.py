from Calculate_the_area_module_1 import *

Users_choice = input("Area of wich figure do you want to calculate? (Rectangle, Triangle or Circle) ")
if Users_choice == "Rectangle":
    square_of_rectangle(int(input("First side: ")),int(input("Second side: ")))
elif Users_choice == "Triangle":
    square_of_triangle(int(input("The height of triangle: ")),int(input("One side: ")),)
elif Users_choice == "Circle":
    square_of_circle(int(input("Radius of circle: ")))
else:
    print ("You have to choose between Rectangle, Triangle or Circle")