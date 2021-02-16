def reverse(st):
    y = st.split()
    y.reverse()
    x = " "
    for i in y:
        x += " " + i.strip()
    return str(x.strip())