number = int(input("Numbers:"))

digit1 = number // 1000
digit2 = number //100 % 10
digit3 = number // 10 % 10
digit4 = number % 10
mult = digit1*digit2*digit3*digit4
print('Mult:', mult)

num_rev = int(str(number)[::-1])
print("Rev:", num_rev)

num_sort = str(number)
print("Sort:", sorted(num_sort))


