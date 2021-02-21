from random import randint

random_number = randint(1, 100)


def message(text):
    """
    Print message.
    """

    print(text)


def compare(entered_number, rn=random_number):
    """
    The function compares the entered number with a random number
    and returns one of the values.
    """

    number = int(entered_number)
    if number == 0:
        message("You are out of the game")
        return True
    elif number > rn:
        message(f"{number} > ?")
    elif entered_number < rn:
        message(f"{number} < ?")
    else:
        message(f"You won, this is the number: {number}")
        return True


while True:
    message("To exit the game, press: 0")
    enter_number = input("Enter number 1-100: ")
    returned_value = compare(enter_number)
    if returned_value:
        break
