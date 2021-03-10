def dayName(day_num):

		days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		return days[day_num-1] if 0 < day_num <= len(days) else None

try:
	day_num = int(input('Enter the number of the day in the week :  '))
	if day_num == int(day_num):
		print(dayName(day_num))

except ValueError as e:
	print("You should entered a number")

