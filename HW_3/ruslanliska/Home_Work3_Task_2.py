#mult all 4 digits
number = int(input("Enter your 4 digits number: "))
digit_1 = number // 1000
digit_2 = number // 100 % 10
digit_3 = number // 10 % 10 
digit_4 = number % 10

print('Multiplying of all entered digits:', digit_1*digit_2*digit_3*digit_4)

#typing reversed number
reversed_number = str(number)
print("This is reversed list of numbers: ", reversed_number[::-1])

#sort of digits
sorted_number = str(number)
print("Here is sorted numbers: ", sorted(sorted_number))


