x = int(input())
a = x // 1000
b = x // 100 % 10
c = x % 100 // 10
d = x % 10
#print( a, b, c, d)
print(f"Добуток чисел {a}, {b}, {c}, {d} =", a*b*c*d)
print("Реверсне число =", int(str(d)+str(c)+str(b)+str(a)))
s = [a,b,c,d]
s.sort()
print("Посортоване число від меншого до більшого =", str(s[0])+str(s[1])+str(s[2])+str(s[3]))
