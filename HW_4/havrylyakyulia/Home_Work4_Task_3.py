num = int(input("Number:"))

num_1 = 0
num_2 = 1
if num < 2:
    print("Not bad")
else:
    print(num_1, end=' ')
    print(num_2, end=' ')
    for i in range(2, num):
        new_num = num_1 + num_2
        num_1 = num_2
        num_2 = new_num
        print(new_num, end=' ')
        