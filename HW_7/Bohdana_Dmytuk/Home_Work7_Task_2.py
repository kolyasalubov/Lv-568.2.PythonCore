
import re
is_it_good = False
print("now we need to validate your password")

def validation(passw):

    lower_case=False
    upper_case=False
    numbers=False
    signs=False
    length1=False
    length2=False

    if len(re.findall("[a-z]", passw)) != 0:
        lower_case = True
    
    if len(re.findall("[A-Z]", passw)) != 0:
        upper_case = True
    
    if len(re.findall("\d", passw)) != 0:
        numbers = True
    
    if len(re.findall("['$', '#', '@']", passw)) == True:
        signs = True
    
    if len(passw)>=6:
        length1 = True
    
    if len(passw)<=12:
        length2 = True



    return lower_case*upper_case*numbers*signs*length1*length2


password = str(input("""
    enter you passowrd, please
    """))
if validation(password)==False:
    print("that password is not valid")
else:
    print("it is correct")





