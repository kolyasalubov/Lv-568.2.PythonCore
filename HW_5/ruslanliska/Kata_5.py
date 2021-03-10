def count_sheeps(sheep):
    quantity = 0
    for i in sheep:
        if i == True:
            quantity += 1
    return quantity