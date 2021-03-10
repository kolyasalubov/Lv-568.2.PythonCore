def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        t, n = 0, 0
        for i in arr:
            if i < 0:
                n += i
            elif i > 0:
                t += 1
        return [t, n]