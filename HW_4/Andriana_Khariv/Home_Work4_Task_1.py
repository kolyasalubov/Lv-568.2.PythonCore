number = int(input("n = "))
factorial = 1
for i in range(2, number+1):
    factorial *= i
print("n! =", factorial)
