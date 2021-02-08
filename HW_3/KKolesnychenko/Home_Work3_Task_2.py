num=int(input("Задайте четырехзначное число:"))
digit1=num%10
digit2=num//10%10
digit3=num//100%10
digit4=num//1000
mult=digit1*digit2*digit3*digit4
print("Произведение= {}".format(mult))
num_reverse=int(str(num)[::-1])
print("Реверсный порядок:",num_reverse)
num_list=list(str(num))
num_list.sort()
num3=int(''.join(num_list))
print("Сортировка чисел: {}".format(num3))


