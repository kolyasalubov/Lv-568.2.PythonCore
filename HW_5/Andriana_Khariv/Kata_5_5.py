def count_sheeps(array1):
    sheep = 0
    for n in array1:
        if n == True:
            sheep = sheep + 1
    return sheep
