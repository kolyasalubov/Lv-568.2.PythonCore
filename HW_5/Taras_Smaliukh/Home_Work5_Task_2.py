login = "First"

while True:
	your_login = input('Enter you login :   ')
	if your_login == login:
		print('Hi, you!')
		break
	else:
		print('You entered wrong login, please try again')
		continue