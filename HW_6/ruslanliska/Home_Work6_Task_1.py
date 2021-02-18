def largest_number(a, b):
    """The function returns bigger numbers
    Input is 2 digits
    Output is bigger number
    """
    # a = input("Please enter first number: ")
    # b = input("Please enter second number: ")
    if a>b:
        return ("First number {} is bigger than second number {}".format(a, b))
    elif a == b:
        return ("First number {} is equal to second number {}".format(a, b))
    else:
        return ("Second number {} is bigger than first number {}".format(b, a))

print(largest_number(17,16))

print(largest_number.__doc__)