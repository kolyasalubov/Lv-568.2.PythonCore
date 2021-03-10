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


