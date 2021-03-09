#Напишіть програму Python для перевірки дійсності пароля (введення від користувачів).

#Перевірка:
#Принаймні 1 буква між [a-z] та 1 буква між [A-Z].
#Принаймні 1 число між [0-9].
#Принаймні 1 символ із [$ # @].
#Мінімальна довжина 6 символів.
#Максимальна довжина 16 символів.


def getPassword():
   return input("Enter password: ")

def CountDigitsFor(password):
   return sum(character.isdigit() for character in password)

def validPassword(password):
    if len(password) >= 16:
        print('Пароль задовгий')
    elif password.isalnum():
        print('пароль містить цифри')
    else:
        print('фіг зна що')


def main():
   password = getPassword()
   if validPassword(password):
      print(password + " is valid")
   else:
      print(password + " is invalid")

main()
