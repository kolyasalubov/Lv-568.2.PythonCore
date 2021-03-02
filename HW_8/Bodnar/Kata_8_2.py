def list_animals(animals):
    list = ''
    for i in animals:
        list += str(animals.index(i) + 1) + '. ' + i + '\n'
    return list