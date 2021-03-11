num = int(input("Your num:"))

if num < 0:
   print("Error")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print(sum)