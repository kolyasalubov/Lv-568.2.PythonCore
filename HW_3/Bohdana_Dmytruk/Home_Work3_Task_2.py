number = str(input("Type four-digit number"))
product_of_each_number = int(number[0])*int(number[1])*int(number[2])*int(number[3])
print("product of each number is ", product_of_each_number)

number_list = list(number)
#print(number_list)
print("reversed number is ", number_list[3], number_list[2], number_list[1], number_list[0])
print("sorted is ", sorted(number_list))