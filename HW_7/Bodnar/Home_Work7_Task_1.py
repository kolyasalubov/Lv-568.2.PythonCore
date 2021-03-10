from Squares1 import *

selected_figure = input("The square of what figure do you want to calculate: rectangle, triangle or circle? ").lower()
allowed_figures = ["rectangle", "triangle", "circle"]
while selected_figure not in allowed_figures:
    selected_figure = input("You have typed wrong figure, please try again: ").lower()
if selected_figure == "rectangle":
    a, b = int(input("Type the size of the first side ")), int(input("Type the size of the second side "))
    rect_sq = rectangle(a,b)
    print(f"The square of rectangle = {rect_sq}")
elif selected_figure == "triangle":
    h, a = int(input("Type the height of the triangle ")), int(input("Type the size of some side of the triangle "))
    trian_sq = triangle(h,a)
    print(f"The square of triangle = {trian_sq}")
else:
    r = int(input("Type the radius of the circle "))
    circle_sq = circle(r)
    print(f"The square of circle = {circle_sq}")