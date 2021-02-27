def greet(name):
    if name == "Johnny":
        return "Hello, my love"
    else:
        return f"Hello, {name}"
greet_name = input("Enter yout name: ")
print(greet(greet_name))