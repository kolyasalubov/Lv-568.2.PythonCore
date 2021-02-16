x = int(input())
x = list(range(x+1))
x.pop(0)
y = 1
for i in x:
     y *= i
print(f"х! = {y}")