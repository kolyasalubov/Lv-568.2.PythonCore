import re
password = input("Enter your password: ")
if re.findall("[a-z]", password) == []:
    print("Ooops! At least 1 lowercase letter")
elif re.findall("[A-Z]", password) == []:
    print("Ooops! At least 1 capital letter")
elif re.findall("\d", password) == []:
    print("Ooops! At least 1 number")
elif re.findall("[$ # @]", password) == []:
    print("Ooops! At least 1 symbol like [$#@]")
elif len(password) <= 6:
    print("Ooops! Must be minimum 6 characters")
elif len(password) >= 16:
    print("Ooops! Must be maximum 16 characters")
else:
    print("Ok, your password is good")

