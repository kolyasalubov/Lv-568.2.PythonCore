number = int(input())

first_digit = number // 1000
second_digit = number //100 % 10
third_digit = number // 10 % 10
fourth_digit = number % 10


print('Product of digits in', number, 'is', first_digit*second_digit*third_digit*fourth_digit)
print(number, "backwards is", fourth_digit, third_digit, second_digit, first_digit)

number_list = str(number)
print(sorted(number_list))