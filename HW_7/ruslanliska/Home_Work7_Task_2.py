import re

def password_check():
    """This function validates password
    cheks if there is at least 1 capital letter
    if there us more than 6 or less than 16 characters,
    if there at least 1 lowercase letter,
    if there at least 1 specific character and 1 digit
    """
    password = input("Please enter your password: ")
    result_upper = re.findall("[A-Z]", password)
    result_lower = re.findall("[a-z]", password)
    result_digit = re.findall("\d", password)
    result_special = re.findall("[#$@]", password)
    max_len = 16
    min_len = 6
    if len(password) < min_len:
        return "Password must consist at least 6 characters"
    elif len(password) > max_len:
        return "Password must consist no more than 16 characters"
    elif result_upper == []:
        return "Your password is invalid. Password must consist at least 1 capital letter"
    elif result_lower == []:
        return "Your password is invalid. Password must consist at least 1 lowercase letter"
    elif result_digit == []:
        return "Your password is invalid. Password must consist at least 1 digit"
    elif result_special == []:
        return "Your password is invalid. Password must consist at least 1 special symbol (@#$)"
    else:
        return "Your password is valid"
    
print(password_check())

