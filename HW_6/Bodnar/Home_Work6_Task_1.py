def largest_digit(*args):
    """This function returns the largest integer number"""
    return max(args)
x, y = int(input("Enter first number: ")),int(input("Enter second number: "))
num = largest_digit(x,y)
print(f"The largest number is", num)
print(largest_digit.__doc__)