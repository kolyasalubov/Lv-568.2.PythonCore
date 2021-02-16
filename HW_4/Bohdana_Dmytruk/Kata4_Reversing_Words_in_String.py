def reverse(st):
    # Your Code Here
    words=st.split()
    words = list(reversed(words))
    st=" ".join(words)
    return st