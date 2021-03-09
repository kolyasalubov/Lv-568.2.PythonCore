def day_of_week_by_number(weekday_number):
    """
    Display the day of the week by its number,
    if the number is not from 1 to 7, return 'Error'
    """

    day_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        message = day_of_week.get(weekday_number)
        if not message:
            raise ValueError

    except ValueError:
        message = "Day number can be only between '1' and '7'"

    return message


entered_day_number = int(input("Enter number of day: "))
print(day_of_week_by_number(entered_day_number))
