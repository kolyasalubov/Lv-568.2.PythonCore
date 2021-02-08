n = int(input())
d1 = n % 10
d2 = n % 100 // 10
d3 = n % 1000 // 10
d4 = n // 1000
print('Mult:', d1*d2*d3*d4)


y = list(str(n))
y.sort()
a3 = int(''.join(y))
print("Sorting of number:", a3)


revs_n = 0  
while (n > 0):   
    remainder = n % 10  
    revs_n = (revs_n * 10) + remainder  
    n = n // 10   
print("The reverse number is : {}".format(revs_n))  