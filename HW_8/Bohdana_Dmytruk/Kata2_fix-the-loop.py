def list_animals(animals):
    list1 = ''
    m=0
    for i in animals:
        m+=1
        list1 += str(m) + '. ' + i + '\n'
    return list1