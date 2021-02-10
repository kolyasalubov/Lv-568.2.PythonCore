# Change the integer type to a floating type. 

size_of_list = int(input("Enter the number of numbers: "))
entered_numbers = []

while size_of_list != 0:
    entered_numbers.append(int(input("Enter the numbers: ")))
    size_of_list -= 1
# Test output
print(entered_numbers, type(entered_numbers), type(entered_numbers[0]))

for i in range(len(entered_numbers)):
    entered_numbers[i] = float(entered_numbers[i]) 
# Test output
print(entered_numbers, type(entered_numbers), type(entered_numbers[0]))