def count_positives_sum_negatives(arr):
    """
    Return an array, where the first element is the count of positives numbers
    and the second element is sum of negative numbers.

    If the input array is empty or null, return an empty array.
    """

    if not arr:
        return arr
    else:
        first_element = len([item for item in arr if item > 0])
        second_element = sum([item for item in arr if item < 0])
        return [first_element, second_element]


# [10,-65]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# [8,-50]
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
# [1,0]
print(count_positives_sum_negatives([1]))
# [0,-1]
print(count_positives_sum_negatives([-1]))
# [0,0]
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]))
# []
print(count_positives_sum_negatives([]))
