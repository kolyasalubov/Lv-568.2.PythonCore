# Print Fibonacci numbers up to the entered number n.

fibonacci_number_limit=int(input("Enter fibonacci number limit: "))

magic_number_1 =int (False)
magic_number_2 =int (True)

for None_ in range(fibonacci_number_limit):
    magic_number_1, magic_number_2 = magic_number_2, magic_number_1 + magic_number_2
    if magic_number_1 < fibonacci_number_limit:
        print(magic_number_1, end=' ')
    else:
        break