import Home_Work_Task1

choice=input("Enter the geometric shape you want to calculate(rectangle, triangle and circle) ")
if choice=="rectangle":
    height=int(input("Enter the height of a rectangle: "))
    width=int(input("Enter the width of a rectangle: "))
    Home_Work_Task1.rectangle_calculate(height,width)
elif choice=="triangle":
    side_a=int(input("Enter the side A of a triangle: "))
    height=int(input("Enter the height of a triangle: "))
    Home_Work_Task1.triangle_calculate(side_a,height)
else:
    radius=int(input("Enter the radius of a circle: "))
    Home_Work_Task1.circle_calculate(radius)
