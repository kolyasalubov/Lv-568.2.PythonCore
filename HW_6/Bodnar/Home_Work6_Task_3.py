def number_char(arg):
    text = set(arg)
    z = {i: arg.count(i) for i in text}
    return z
x = input("Введіть текст: ")
d = number_char(x)
for a in d:
    print(f"Кількість символу \"{a}\" в тексті = {d[a]}")