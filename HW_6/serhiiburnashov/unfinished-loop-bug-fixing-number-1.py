def create_array(n):
    """Help Timmy find and fix the bug in his unfinished for loop!"""

    res = []
    i = 1
    while i <= n: 
        res.append(i)
        i += 1
    return res


print(create_array(7))
