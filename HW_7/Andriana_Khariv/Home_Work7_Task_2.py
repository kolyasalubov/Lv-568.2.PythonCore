#Перевірка:
#Принаймні 1 буква між [a-z] та 1 буква між [A-Z].
#Принаймні 1 число між [0-9].
#Принаймні 1 символ із [$ # @].
#Мінімальна довжина 6 символів.
#Максимальна довжина 16 символів.

#не робоча програма

import re

password = input("Enter password: ")

if len(password) >= 16:
    print('Пароль задовгий')
elif re.findall("[0-9]", password) == []:
    print('Пароль повинен містити цифри')
elif re.findall("[a-z]", password) == []:
    print("Пароль не містить букви нижнього регістру")
elif re.findall("[A-Z]", password) == []:
    print("Пароль не містить букви верхнього регістру")
elif re.findall("[#@$]", password) == []:
    print("Пароль не містить символів #, @ або $")
elif len(password) <= 6:
    print("Пароль закороткий")
else:
    print(password + ' супер пароль')


