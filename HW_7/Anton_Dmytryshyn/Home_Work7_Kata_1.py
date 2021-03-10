def count_positives_sum_negatives(arr):
    count = 0
    sum_neg = 0
    if arr == []:
        return arr
    else:
        for el in arr:
            if el>0:
                count += 1
            elif el<0:
                sum_neg +=el
    return [count, sum_neg]