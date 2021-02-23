test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = []
list2 = []
list3 = []
for num in test_list:
    if num % 2 == 0:
        list1.append(num)
    elif num % 3 == 0:
        list2.append(num)
    else:
        list3.append(num)
print(f"{list1} is divisible by 3")
print(f"{list2} is divisible by 3")
print(f"{list3} is not divisible by 2 and 3")
