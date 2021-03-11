week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

try:
    x = int(input("Type any digit from 1 to 7: "))
    if 0 < x <= len(week):
        print(f"{x} is {week[x-1]}")
    elif x > 7 or x <= 0:
        print(f"Error. There is no {x} days in a week")
except ValueError:
     print("Error. You should type only integer digit.")