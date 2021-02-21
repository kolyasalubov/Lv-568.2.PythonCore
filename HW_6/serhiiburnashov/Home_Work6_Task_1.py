def largest_number_of_two_numbers(first, second):
    """This function returns the largest number of two numbers."""

    largest_num = max(first, second)
    return largest_num


first_number, second_number = (
    int(input("Enter first number: ")),
    int(input("Enter second number: "))
)
largest_number = largest_number_of_two_numbers(first_number, second_number)
print(f"The largest number is: {largest_number}")
print(largest_number_of_two_numbers.__doc__)
