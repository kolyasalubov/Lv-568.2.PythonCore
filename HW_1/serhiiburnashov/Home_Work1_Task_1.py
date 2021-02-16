# Output the question to the console 
# Input answer
# Output the information and answers of user


entered_user_name, entered_user_age, entered_user_city = (
    input("What is your name? "), 
    input("How old are you? "),
    input("Where do you live? "))

print(  "\n" + "\"Hello, "       + entered_user_name + "\"," + 
        "\n" + "\"Your age is "  + entered_user_age  + "\"," + 
        "\n" + "\"You live in "  + entered_user_city + "\".")