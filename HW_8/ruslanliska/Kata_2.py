def list_animals(*animals):
    animal_list = ''
    for i in range(len(animals)):
        animal_list += str(i + 1) + '. ' + "".join(animals[i]) + '\n'
    return animal_list

print(list_animals("dog", "cat"))