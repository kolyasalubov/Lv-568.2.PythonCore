def max_num (a,b):
    if a>=b:
        return a
    else:
        return b

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print('Max number is ', max_num(a,b))