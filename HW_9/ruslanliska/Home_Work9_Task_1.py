def age_defining():
    """Defining whether age is even or odd and returns it to user
    If age under 0, raising ValueError
    """
    age = int(input("Enter your age: "))
    if age <=0 0:
        raise ValueError("Age cannot be less than 0")
    elif age % 2 == 0:
        return f"Your age {age} is even"
    elif age % 2 !=0:
        return f"Your age {age} is odd"
