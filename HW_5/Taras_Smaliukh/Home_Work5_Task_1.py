even_num = []
odd_num = []
other_num = []

for i in range(1,10):
	if i % 2 == 0:
		even_num.append(i)
for i in range(1,10):
	if i % 3 == 0:
		odd_num.append(i)
for i in range(1,10):
	if i % 2 != 0 and i % 3 != 0:
		other_num.append(i)


print(even_num)
print(odd_num)
print(other_num)
