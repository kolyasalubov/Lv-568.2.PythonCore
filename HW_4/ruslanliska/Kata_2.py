def reverse(st):
    st = st.split()
    result = st[::-1]
    return " ".join(result)
print(reverse("Hi there"))