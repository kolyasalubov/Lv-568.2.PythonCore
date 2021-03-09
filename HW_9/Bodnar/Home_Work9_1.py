try:
    def age(x):
        if x % 2 == 0 and x > 0:
            return "Your age is even"
        elif x % 2 == 1 and x > 0:
            return "Your age is odd"
        elif x < 0:
            raise ValueError("Age can't have negative number")
    x = int(input("Your age?  "))
    print(age(x))
except ValueError as e:
    print(e)