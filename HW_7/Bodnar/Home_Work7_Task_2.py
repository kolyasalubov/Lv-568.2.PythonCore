import re
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
y = [a, b, c, d, e, f]
while 0 in y:
    x = input("Type your password: ")
    a = re.findall("[a-z]", x)
    if len(a) == 0:
        print("Error. The password should includes at least one letter between [a-z]")
        a = 0
    b = re.findall("[A-Z]",x)
    if len(b) == 0:
        print("Error. The password should includes at least one letter between [A-Z]")
        b = 0
    c = re.findall("\d",x)
    if len(c) == 0:
        print("Error. The password should includes at least one digit")
        c = 0
    d, e = len(x), len(x)
    if d < 6:
        print("Error. The min symbols could be 6")
        d = 0
    if e > 16:
        print("Error. The max symbols could be 16")
        e = 0
    f = re.findall("[$, #, @]",x)
    if len(f) == 0:
        print("Error. Password should includes at least on of these symbols: #, $, @")
        f = 0
    y = [a,b,c, d, e, f]
else:
    print("The password is correct")