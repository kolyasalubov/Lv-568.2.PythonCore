users_input = input("Please type any word or text: ")

def characters_counter (users_input):
    """This function counts how many times each character is found"""
    for i in users_input:
        print ("Character", i, "is found", users_input.count(i), "times in", users_input)

characters_counter(users_input)