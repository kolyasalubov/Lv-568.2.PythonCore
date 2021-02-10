my_list = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]

for element in my_list:
    if element % 2 == 0:
        print (element, "is divisible by 2")

for element in my_list:
    if element % 3 ==0:
        print (element, "is divisible by 3")

for element in my_list:
    if element % 2 !=0 and element % 3 !=0:
        print (element, "is not divisible by 2 and 3")