def solution(number):
    funct_sum = []
    if number == 0:
        return 0
    else:
        for i in range(1,number):
            if i % 3 == 0 or i % 5 == 0:
                funct_sum.append(i)
        return sum(set(funct_sum))