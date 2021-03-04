def count_positives_sum_negatives(arr):
    count_positive=0
    arr_negative=[]
    if not arr:
        return []
    else:
        for i in range(len(arr)):
            if arr[i]>0:
                count_positive+=1
            else:
                arr_negative.append(arr[i])
        return [count_positive,sum(arr_negative)]