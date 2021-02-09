first_variable = input("Enter first variable: ")
second_variable = input("Enter second variable: ")

print(  "Before:"  )
print(  "First variable:", first_variable, 
        "Second variable:", second_variable  )

first_variable, second_variable = second_variable, first_variable

print(  "After:"  )
print(  "First variable:", first_variable, 
        "Second variable:", second_variable  )