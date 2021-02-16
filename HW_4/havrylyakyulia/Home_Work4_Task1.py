num = int(input("Number: "))

factorial = 1

if num == 0:
    print("Factorial always 1, according to the convention for an empty product")
else: 
    for i in range (2, num + 1):
        factorial *= i
    print("Factorial:", factorial)



