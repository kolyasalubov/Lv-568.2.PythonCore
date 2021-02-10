#a = range(11)
#for x in a:
    #if x % 2 == 0:  
       # print(x) 
        #continue
#print("This numbers are divisible by 2")

#a = range(11)
#for x in a:
    #if x % 3 == 0:  
       # print(x) 
        #continue
#print("This numbers are divisible by 3")

a = range(11)
for x in a:
    if x % 2 != 0 and x % 3 != 0:  
        print(x) 
        continue
print("This numbers are not divisible by 2 and 3")