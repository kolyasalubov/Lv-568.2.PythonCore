oper = str(input("""
enter the numbers of operations you want to use:
1 = find square of rectangle
2 = find square of circle
3 = find square of triangle

"""))
def rect_square (a, b):
    s = a*b
    return s

def circle_square (r):
    P=3.14
    s = P*r**2
    return s

def trian_square (c, h):
    s = 1/2*c*h
    return s

for i in oper:
    if i=='1':
        a = int(input("enter first side of rectangle "))
        b = int(input("enter second side of rectangle "))
        print("square of rectangle is: ", rect_square(a, b))
    elif i=='2':
        r = int(input("enter radius of circle "))
        print("square of circle is: ", circle_square(r))
    elif i=='3':
        m = int(input("enter side of triangle "))
        f = int(input("enter height of triangle "))
        print("square of triangle is: ", trian_square(m, f))
    else:
        print("try again and enter valid information")