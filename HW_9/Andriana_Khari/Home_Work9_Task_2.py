#Write a program that analyzes the entered
# number and, depending on the number, gives
# the day of the week that corresponds to this
# number (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers
# from 8 and more, as well as cases of entering
# non-numerical data.


week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    day = int(input("enter a number from 1 to 7 that corresponds to the day of the week: "))
    if 0 < day <= len(week_day):
        days = week_day[day-1]
        print(day, "is", days)
    elif day > 7:
        print("there are no", day, "days in a week", )
    elif day <= 0:
        print("there are no negative days in a week")
except ValueError:
    print("wrong data format")
