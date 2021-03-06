DayNumbers = {
    1:"Monday", 2:"Tuesday",
    3:"Wednesday", 4:"Thursday",
    5:"Friday", 6:"Saturday", 7:"Sunday",
}

try:
    number = int(input("Enter the number of the day: "))
    print (DayNumbers[number])
except:
    print("Error, day number can be only between 1 and 7")