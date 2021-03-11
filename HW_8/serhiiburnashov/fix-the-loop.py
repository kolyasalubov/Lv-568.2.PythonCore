def list_animals(animals_):
    """
    If you pass the list of your favorite animals to the function,
    you should get the list of the animals with orderings and newlines added.
    """

    list_ = ''
    for i in range(len(animals_)):
        list_ += str(i + 1) + '. ' + animals_[i] + '\n'
    return list_


# '1. dog\n2. cat\n3. elephant\n'
animals = ['dog', 'cat', 'elephant']
print(list_animals(animals))
