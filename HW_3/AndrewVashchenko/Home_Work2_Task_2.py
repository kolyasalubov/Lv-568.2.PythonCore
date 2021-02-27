fourDigit = int(input("Input a 4-digit integer: "))
first = fourDigit//1000
second = fourDigit//100
third = fourDigit//10
fourth = fourDigit//1

print('Our digit is', fourDigit)
print("Sum of its nums is:", first*second*third*fourth)
type_str = str(fourDigit)
print('Reverse engeneering: ', type_str[::-1])
print("Sorted int: ", sorted(type_str))