def double_char(s):
    new_str=[]
    for i in s:
        i+=i
        new_str.append(i)
    new_str=''.join(new_str)
    return new_str