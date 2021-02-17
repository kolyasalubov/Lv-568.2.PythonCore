def calc_num_char(strings):
    dict = {}
    for i in strings:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return dict
print(calc_num_char(str(input("Strings: "))))