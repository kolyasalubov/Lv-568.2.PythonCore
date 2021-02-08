num=int(input("Enter number: "))
if num==0 and num==1:
    factorial=1
    print(f"Factorial = {factorial}")
elif num<0:
    print("Error")
else:
    factorial=1
    for i in range(1,num+1):
        factorial*=i
        i+=1
    print(f"Factorial = {factorial}")