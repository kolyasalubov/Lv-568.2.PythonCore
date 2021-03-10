from random import randint

d = randint(1, 100)
x = int(input("Type the number between 1 and 100: "))
while x != d:
    if x > d:
        x = int(input("You have typed bigger number, try again: "))
    else:
        x = int(input("You have typed smaller number, try again: "))
print(f"You are right, the number is {d}")
