#fib1 = 1
#fib2 = 1

#n = int(input())

#for i in range(2, n):
    #fib1, fib2 = fib2, fib1 + fib2
    #print(fib2, end=' ')
#print()

entered_num = int(input())
fib=[0,1]
for i in range(entered_num+1):
    if fib[i]+fib[i+1]>=entered_num:
        break
    else:
        fib.append(fib[i]+fib[i+1])
        i+=1
print(fib)