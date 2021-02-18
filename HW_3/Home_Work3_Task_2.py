number = int(input("Введіть ціле число:"))

sum = 0
revers_num = 0
sort_num = "".join(sorted(str(number)))

while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
    revers_num = revers_num * 10
    revers_num = digit + revers_num

print("Сума цифр:", sum)
print("Число в реверсному порядку:", revers_num)
print("Посортовані числи в порядку ззростання:", sort_num)
