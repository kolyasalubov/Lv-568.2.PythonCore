def double_char(s):
    s_double = []
    for i in range(len(s)):
        s_double.append(s[i])
        s_double[i] *= 2
    s_double = ''.join(s_double)
    return s_double