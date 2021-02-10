# Enter user login

LOGIN_IN_DATABASE = "First"

while input('Enter your login (True login "First"): ') != LOGIN_IN_DATABASE:
    print('Your login wrong, try again.')
print(f'Hi, {LOGIN_IN_DATABASE}!')