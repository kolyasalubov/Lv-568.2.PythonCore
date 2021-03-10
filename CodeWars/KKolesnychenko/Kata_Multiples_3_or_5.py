def solution(number):
    arr=[]
    if number<0:
        return 0
    else:
        for i in range(number):
            if i%3==0 or i%5==0:
                arr.append(i)
        return sum(arr)   