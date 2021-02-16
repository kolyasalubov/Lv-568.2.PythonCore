a =int(input("enter first number "))
b = int(input("enter second number "))

def bigger_num(a, b):
    """
    function bigger_num 
    input parameter: a, b
    type input parameter - int
    output: bigger number
    """
    if a>b:
        return a
    else:
        return b

print(bigger_num(a,b), "is bigger")
print(bigger_num.__doc__)
