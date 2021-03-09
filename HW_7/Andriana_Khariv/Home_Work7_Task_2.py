#Перевірка:
#Принаймні 1 буква між [a-z] та 1 буква між [A-Z].
#Принаймні 1 число між [0-9].
#Принаймні 1 символ із [$ # @].
#Мінімальна довжина 6 символів.
#Максимальна довжина 16 символів.

#не робоча програма


def getPassword():
   return input("Enter password: ")

def validPassword(password):
    if len(password) >= 16:
        print('Пароль задовгий')
    elif password.isdigit():
        print('пароль не містить цифри')
    elif password.islower() == 0:
        print("неба букви нижнього регістру")
    elif password.isupper() == 0:
        print("нема букви верхнього регістру")
    elif len(password) == "@":
        print("незнаю ще")
    elif len(password) <= 6:
        print("Пароль закороткий")
    else:
        print('супер')

def main():
   password = getPassword()
   if validPassword(password):
      print(password + " валідний")
   else:
      print(password + " не валідний")

main()
