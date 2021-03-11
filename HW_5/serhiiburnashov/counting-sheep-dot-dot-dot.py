def count_sheeps(sheep):
    """
    Function that counts the number of sheep present in the array.
    """

    count = sheep.count(True)
    return count


#17
print(count_sheeps([True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]))
  