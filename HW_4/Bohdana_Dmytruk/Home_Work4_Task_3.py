last_closest_number = int(input("what is the last number in you sequence? "))
if last_closest_number == 1:
        print("[0, 1, 1]")
elif last_closest_number < 0:
    print("number should be positive")
else: 
    list_of_numbers = []
    number = 0
    number_1 = 0
    number_2 = 1
    while number <= last_closest_number:
        new_number =  number_1 + number_2
        number_1 = number_2
        number_2 = new_number
        number = new_number
        if number > last_closest_number:
            break
        list_of_numbers.append(new_number)
    print(list_of_numbers)
        

   
