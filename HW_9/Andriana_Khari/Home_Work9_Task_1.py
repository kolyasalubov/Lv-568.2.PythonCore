#Write a program that prompts the user to enter
# their age, and then displays a message stating
# whether the age is even or odd. The program must
# provide the ability to enter a negative number,
# and in this case generate an exception. The master
# code should call a function that processes the information entered.


try:

    num = int(input("Your age?  "))

    def age(num):
        if num % 2 == 0 and num > 0:
            print("Age", num, "is even")
        elif num % 2 == 1 and num > 0:
            print("Age", num, "is odd")
        elif num < 0:
            raise ValueError("This can't be")

    print(age(num))

except ValueError as err:
    print(err)
