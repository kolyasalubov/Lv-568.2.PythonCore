def count_positives_sum_negatives(input):

    if not input:
        return []

    count_pos = 0
    sum_neg = 0

    for i in input:
        if i > 0:
            count_pos += 1
        elif i < 0:
            sum_neg += element
    return [count_pos, sum_neg]