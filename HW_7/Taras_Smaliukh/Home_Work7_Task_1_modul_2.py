import Home_Work8_Task_1_modul_1


while True:
	your_choise = input("If you want to calculate:\n square of rectangle  enter '1'\n square of triangle enter '2'\n square of circle  square enter '3'\n see you next time 'q'\n")

	if your_choise == '1':
		a = float(input("Enter size 'a':    "))
		b = float(input("Enter size 'b':    "))
		print(Home_Work8_Task_1_modul_1.rectangle_square(a, b))

	elif your_choise == '2':
		a = float(input("Enter size 'a':    "))
		b = float(input("Enter size 'b':    "))
		c = float(input("Enter size 'c':    "))
		print(Home_Work8_Task_1_modul_1.triangle_square(a, b, c))

	elif your_choise == '3':
		a = float(input("Enter the radius:    "))
		print(Home_Work8_Task_1_modul_1.circle_square(a))

	elif your_choise == 'q':
		print("See you")
		break
	else:
		print('Try again')
