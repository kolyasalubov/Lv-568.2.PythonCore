# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

numbers_divisible_by_2 = [
    item for item in range(1,10) if item % 2 == 0]
numbers_divisible_by_3 = [
    item for item in range(1,10) if item % 3 == 0]
numbers_not_divisible_by_2_and_3 = [
    item for item in range(1,10) if item % 2 != 0 and item % 3 != 0]

numbers_divisible_by_2 = str(
    numbers_divisible_by_2).replace('[','').replace(']','')
numbers_divisible_by_3 = str(
    numbers_divisible_by_3).replace('[','').replace(']','')
numbers_not_divisible_by_2_and_3 = str(
    numbers_not_divisible_by_2_and_3).replace('[','').replace(']','')

print(f'Numbers divisible by "2": {numbers_divisible_by_2}', end='.\n')
print(f'Numbers divisible by "3": {numbers_divisible_by_3}', end='.\n')
print(f'Numbers not divisible by "2" and "3": {numbers_not_divisible_by_2_and_3}', end='.')