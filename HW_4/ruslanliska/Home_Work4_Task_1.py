#calculating factorial

number = int(input("Enter your number: "))

factorial = 1

if number == 0:
    print("The factorial is 1")
elif number < 0:
    print("There is no factorial for entered number")
else: 
    for i in range (1, number + 1):
        factorial = factorial*i
    print("The factorial of", number, "is", factorial)