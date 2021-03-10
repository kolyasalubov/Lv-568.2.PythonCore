import re

"""
This program checks if the password, from users input,
is valid, following the next few rules(see comments).
"""

password = input("Please enter the password: ")
check_counter = 0

if len(re.findall("\d", password)) != 0: #checking if there are any digits
    check_counter += 1
if len(password)>=6 and len(password)<=16: #checking the password lenght
    check_counter += 1
if len(re.findall("[@#$]",password)) !=0: #checking if characters @, #, or $ are included
    check_counter += 1
if len(re.findall("[a-z]", password)) != 0 and len(re.findall("[A-Z]", password)) != 0: 
    check_counter += 1                    #checking if a-z and A-Z included

if check_counter == 4:
    print ("Password is valid.")
else:
    print ("Password is not valid.")