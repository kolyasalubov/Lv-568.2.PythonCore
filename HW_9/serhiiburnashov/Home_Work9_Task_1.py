def age_is_even_or_odd(age):
    """ Defining age is even or odd If age less 1, return 'Error' """

    try:
        if age > 0:
            msg = "Even" if age % 2 == 0 else "Odd"
            message = f"Your age: {age}, is {msg}"
        else:
            raise ValueError

    except ValueError:
        message = "You should entered a number and age cannot be less than '1'"

    return message


age = int(input("Enter your age: "))
print(age_is_even_or_odd(age))
