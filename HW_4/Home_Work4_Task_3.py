n = int(input("Введіть число n "))
fib1 = fib2 = 1

print(fib1, end=' ')
print(fib2, end=' ')
while fib2 < n-fib1:
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

