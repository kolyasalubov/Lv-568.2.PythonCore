variable_1 = int(input("Enter your first vatiable: "))
variable_2 = int(input("Enter your second vatiable: "))

print("You have entered:")
print("First variable:", variable_1)
print("Second variable: ", variable_2)

variable_1, variable_2 = variable_2, variable_1
print("But we changed it, and now it looks like:")
print("First variable:", variable_1)
print("Second variable: ", variable_2)
