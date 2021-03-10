def solution(number):
    sum_0f_numbers = sum([i for i in range(1,number) if i % 3 == 0 or i % 5 == 0])
    return sum_0f_numbers
