def double_char(s):
    st = []
    for i in range(len(s)):
        st.append(s[i])
        st[i] *= 2
    st = ''.join(st)
    return st
