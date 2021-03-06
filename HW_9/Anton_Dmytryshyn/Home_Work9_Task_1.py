age = int(input("Please enter your age here: "))


def AgeEvenOdd (age):
    try:
        if age <= 0:
            raise ValueError("Age can not be negative number")    
        if age % 2 == 0:
            print("Your age is an even number")
        else: 
            print("Your age is an odd number")
    except ValueError as e:
        print(e)


AgeEvenOdd(age)
