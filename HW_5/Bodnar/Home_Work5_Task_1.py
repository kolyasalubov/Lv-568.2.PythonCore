x = list(range(1,10))
even = [i for i in range(1,10) if i % 2 == 0]
odd = [z for z in range(1,10) if z % 3 == 0 and z % 2 != 0]
for n in range(1,10):
    if n % 2 == 0 or n % 3 == 0:
        x.remove(n)
print(f"even numbers are {even}")
print(f"odd numbers are {odd}")
print(f"numbers that are not divisible by 2 and 3 are {x}")