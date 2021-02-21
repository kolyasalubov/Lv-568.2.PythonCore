def password_check(password):
    """Check if the password is valid.

    This function checks the following conditions
    if its length is greater than 6 and less than 16
    if it has at least one uppercase letter
    if it has at least one lowercase letter
    if it has at least one numeral
    if it has any of the required special symbols
    """
    Symbol=['$','@','#']
    is_val=True

    true_responde = "The password is valid"
    false_responde = "Not valid"
    if len(password) < 6:
        is_val=False
    if len(password) > 16:
        is_val=False
    if not any(char.isdigit() for char in password):
        is_val=False
    if not any(char.isupper() for char in password):
        is_val=False
    if not any(char.islower() for char in password):
        is_val=False
    if not any(char in Symbol for char in password):
        is_val=False

    if is_val == True:
        return true_responde
   
    else:
        return false_responde

password = input('enter the password : ')
print(password_check(password))