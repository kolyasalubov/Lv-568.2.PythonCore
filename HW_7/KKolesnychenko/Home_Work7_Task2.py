import re

def password_validation(password):
    pattern=re.compile(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(?=.*[$#@].*)[0-9a-zA-Z$#@]{6,16}$')
    if re.findall(pattern,password):
        return print("Your password is correct")
    else:
        return print("Try again")

password_validation(input("Enter your password: "))    