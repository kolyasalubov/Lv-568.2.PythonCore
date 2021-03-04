def count_positives_sum_negatives(arr):
    
    pos, neg  = 0, 0
    
    if arr == []:
        return []

    for a in arr:
        if a > 0:
            pos += 1
        if a < 0:
            neg += a
    return [pos, neg]
