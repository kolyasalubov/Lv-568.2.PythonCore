def solution(number):
    """
    Function return the sum of all the multiples of 3 or 5 below the number passed in.
    """

    sum_number_multiples_3_5 = sum(
        [item for item in range(number) if item % 3 == 0 or item % 5 == 0]
    )
    return sum_number_multiples_3_5


# 23
print(solution(10))
