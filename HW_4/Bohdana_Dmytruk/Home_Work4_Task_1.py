import math
number = int(input("enter a number to calculate factorilal"))
if number == 1:
    print(f"{number}! is {number}")
elif number > 1:
        print(f"{number}! is", math.factorial(number))
else:
    print("unable to calculate")



