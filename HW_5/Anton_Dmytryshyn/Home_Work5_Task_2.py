Login_Data = {"Login": "First"}
while input ("Please enter your login: ") == Login_Data["Login"]:
    print ("Greetings User!")
    break
else:
    print ("Error - login is incorrect")