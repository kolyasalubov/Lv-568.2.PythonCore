size_of_list = int(input("how many numbers you list contains? "))
number_list = [] 
for i in list(range(size_of_list)):
        number_list.append(int(input("enter a number to turn it into float "))) 
print((number_list))

for j in number_list:
    floated = float(j)
    print(floated)
