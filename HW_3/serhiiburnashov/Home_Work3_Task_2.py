entered_number = int(input("Enter 4-digit number: "))

first_digit = entered_number // 1000
second_digit = entered_number // 100 % 10
third_digit = entered_number // 10 % 10
fourth_difgit = entered_number % 10

numbers_list = []
numbers_list.append(first_digit)
numbers_list.append(second_digit)
numbers_list.append(third_digit)
numbers_list.append(fourth_difgit)

print("Product of digits:", 
        numbers_list[0], 
        numbers_list[1], 
        numbers_list[2], 
        numbers_list[3], 
        "is:", 
        numbers_list[0] * 
        numbers_list[1] * 
        numbers_list[2] * 
        numbers_list[3])
        
reverse_numbers_list = ''.join(str(numbers_list[::-1]).split(","))
write_reverse_numbers_list = int(reverse_numbers_list.replace('[','').replace(' ','').replace(']',''))
print("Reverse numbers:", write_reverse_numbers_list)

sort_numbers_list = ''.join(str(sorted(numbers_list)).split(","))
write_sort_numbers_list = int(sort_numbers_list.replace('[','').replace(' ','').replace(']',''))
print("Reverse numbers:", write_sort_numbers_list)
