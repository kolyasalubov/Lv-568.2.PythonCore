number = int(input("Enter your number:"))
a = 0
b = 1

if number == 1:
    print(a)
elif number < 0:
    print("Please, enter number above 0")

else:
    print(a)
    print(b)
    for i in range(2, number):
        c = a + b
        a = b
        b = c
        print(c)
        if a + b >= number:
            break