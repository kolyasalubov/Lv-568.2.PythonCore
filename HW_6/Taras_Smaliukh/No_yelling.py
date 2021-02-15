def filter_words(st):
    # Your code here.
    st = st.strip()
    st = ' '.join(st.split())

    return st.capitalize()