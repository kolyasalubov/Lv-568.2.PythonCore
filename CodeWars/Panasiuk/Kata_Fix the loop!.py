def list_animals(animals):
    result =''
    for i in animals:
        result += str(animals.index(i)+1)+'. '+ i+'\n'
    return result