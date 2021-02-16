def filter_words(st):
    st_to_list = st.split()
    st_with_normal_spacing = ' '.join(st_to_list)
    first_one = st_with_normal_spacing[0].upper()
    rest = st_with_normal_spacing[1:].lower()
    return first_one + rest