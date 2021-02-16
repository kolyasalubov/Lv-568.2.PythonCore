my_str=input("enter string ")
my_str = my_str.lower()
str_characters = set(my_str)
print(my_str)

def number_of_char (your_string, your_characters):
    counter=0
    for i in your_characters:
        for j in your_string:
            if i==j: counter+=1
        print(f"number of '{i}' is {counter}")
        counter = 0

number_of_char(my_str, str_characters)
