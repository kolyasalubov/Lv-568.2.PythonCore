def reverse_list(l):
    """
    Function that takes in a list and returns a list with the reverse order.
    """

    l.reverse()
    return l


# [4, 3, 2, 1]
print(reverse_list([1, 2, 3, 4]))
# [4, 5, 1, 3]
print(reverse_list([3, 1, 5, 4]))
# [2, 9, 6, 3]
print(reverse_list([3, 6, 9, 2]))
# [1]
print(reverse_list([1]))
