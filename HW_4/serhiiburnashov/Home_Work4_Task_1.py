#Calculate the number n factorial

entered_factorial = int(input("Enter factorial of number: "))
temp = entered_factorial

if entered_factorial > 0:
    for i in range(1, entered_factorial):
        temp *= i
elif entered_factorial == 0:
    temp = 1
else:
    temp = 'Enter number ">" or "=" 0'

print(f"{entered_factorial}! = {temp}")
