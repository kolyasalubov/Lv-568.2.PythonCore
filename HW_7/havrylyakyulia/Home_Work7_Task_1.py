import Home_Work7_Task_1_module1
choice = input("What do you want? rectangle(1),triangle(2),circle(3):")
if choice == '1':
    a = int(input("Side a: "))
    b = int(input("Side b: "))
    print(Home_Work7_Task_1_module1.rectangle_square(a, b))
elif choice == '2':
    a = int(input("Side a: "))
    b = int(input("Height b: "))
    print(Home_Work7_Task_1_module1.triangle_square(a, b))
elif choice == '3':
    r = int(input("Radius: "))
    print(Home_Work7_Task_1_module1.circle_square(r))
else:
    print("Error") 