def filter_words(st):
    """Write a function taking in a string like WOW this
    is REALLY amazing and returning Wow this is really amazing. 
    String should be capitalized and properly spaced. 
    Using re and string is not allowed."""

    filtered = " ".join(st.capitalize().split())
    return filtered


print(filter_words('HELLO world!'))
