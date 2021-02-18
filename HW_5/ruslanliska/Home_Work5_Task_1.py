#even numbers that are divisible by 2,
number_divisible_2 = []
for i in range(1, 11):
    if i % 2 == 0:
        number_divisible_2.append(i)

print("Numbers is divisible by 2:", number_divisible_2)

#odd numbers, which are divisible by 3,
number_divisible_3 = []  

for i in range(1, 11):
    if i % 3 == 0:
        number_divisible_3.append(i)

print("Odd numbers which is divisible by 3:", number_divisible_3)

#numbers that are not divisible by 2 and 3.
number_not_divisible_2_3 = []

for i in range(1, 11):
    if i % 3 != 0 and i % 2 !=0:
        number_not_divisible_2_3.append(i)
print("Here is numbers not divisible by 2 and 3", number_not_divisible_2_3)