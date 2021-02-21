def calculates_the_number_of_characters_in_a_string(text):
    """Function that calculates the number of characters included in a given string"""

    return len(text)


entered_string = input("Enter text: ")
number_of_characters = calculates_the_number_of_characters_in_a_string(entered_string)
print(f"Number of characters included in a given string: {number_of_characters}")
