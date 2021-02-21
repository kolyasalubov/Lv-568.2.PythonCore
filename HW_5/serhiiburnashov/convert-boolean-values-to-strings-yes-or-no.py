def bool_to_word(boolean):
    """
    Method that takes a boolean value and return a 
    "Yes" string for true, or a "No" string for false.
    """

    message = "Yes" if boolean else "No"
    return message


#Yes
print(bool_to_word(True))
#No
print(bool_to_word(False))
