n = int(input())
fib = [0,1,1]
while n not in range(fib[-1]+1):
    fib.append(fib[-2]+fib[-1])
print(fib)