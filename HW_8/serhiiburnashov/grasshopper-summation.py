def summation(num):
    """
    Function that finds the summation of every number from 1 to num.
    """

    result = sum(list(range(num + 1)))
    return result


# 1
print(summation(1))
# 36
print(summation(8))
# 253
print(summation(22))
# 5050
print(summation(100))
# 22791
print(summation(213))
