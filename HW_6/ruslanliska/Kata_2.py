def filter_words(st):
    st=st.lower()
    st=st.capitalize()
    result = " ".join(st.split())
    return result