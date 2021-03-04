def solution(number):

        num_list=[]
        for a in range (number):
            if a%3 == 0:
                num_list.append(a)
            elif a%5 == 0:
                num_list.append(a)
        print(sum(num_list))

solution(10)
