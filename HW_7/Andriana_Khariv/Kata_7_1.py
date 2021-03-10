def count_positives_sum_negatives(arr):
    if not arr:
        return []
    n1 = 0
    n2 = 0
    for i in arr:
        if i > 0:
            n1 += 1
        elif i < 0:
            n2 += i
    return [n1, n2]
