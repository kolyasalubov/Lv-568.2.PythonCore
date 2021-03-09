def list_animals(animals):
    res = ''
    for i in range(len(animals)):
        res += str(i + 1) + '. ' + "".join(animals[i]) + '\n'
    return res
