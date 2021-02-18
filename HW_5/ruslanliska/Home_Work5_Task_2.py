login = "First"
running = True

while running:
    enter_login = input("Enter your login: ")
    if enter_login == login:
        print("Hello! We are glad to see you here!")
        running = False
    else:
        print("We are sorry, enter the correct login")