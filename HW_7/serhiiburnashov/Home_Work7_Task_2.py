import re


def validation(password):
    """
    Password check.
    """

    password_check = re.fullmatch(r'^.*(?=.*[a-z])(?=.*?[A-Z])(?=.*\d)(?=.*?[@$#])'
                                  r'[a-zA-Z0-9@$#]{6,16}$', password)
    return password_check


entered_password = input("Enter password to test: ")

check = validation(entered_password)
if check:
    print(f"Valid password, len password: {len(entered_password)}")
else:
    print(f"Password not valid, len password: {len(entered_password)}")
