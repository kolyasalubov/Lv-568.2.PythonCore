def count_positives_sum_negatives(arr):
    #your code here
    positive = 0
    negative = 0
    for i in arr:
        if i>0:
            positive+=1
        else:
            negative+=i
    if arr==[]:
        return []
        
    return [positive, negative]