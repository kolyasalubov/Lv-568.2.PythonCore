def numb_days_func():
    """analyzes the entered number and, depending on the number, 
    gives the day of the week that corresponds to this number 
    """
    number_days = [1, 2, 3, 4, 5, 6, 7]
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = dict(zip(number_days, all_days))
    num = int(input("Enter your number: "))
    if 0 < num < 8:
        return day[num]
    else:
        raise ValueError("There is no such a day. We have only 7 days(1-7)")

# print(numb_days_func())