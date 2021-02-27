def solution(number):
    num_list = []
    for i in range(number):
        if i%3==0:
            num_list.append(i)
        elif i%5==0:
            num_list.append(i)
        else:
            continue
    number=0
    for j in num_list:
        number+=j
    return number