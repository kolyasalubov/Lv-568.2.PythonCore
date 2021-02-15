def string_counter(n):
    dict = {}
    for k in n:
        keys = dict.keys()
        if k in keys:
            dict[k] += 1
        else:
            dict[k] = 1
    return dict

a=str(input("Please, enter your string: "))
print(string_counter(a))