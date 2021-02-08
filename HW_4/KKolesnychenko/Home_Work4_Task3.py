entered_num=int(input("Enter number: "))
fib=[0,1]
for i in range(entered_num+1):
    if fib[i]+fib[i+1]>=entered_num:
        break
    else:
        fib.append(fib[i]+fib[i+1])
        i+=1
print(fib)