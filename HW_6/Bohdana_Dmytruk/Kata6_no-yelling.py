def filter_words(st):
    # Your code here.
    whole = st[0].upper() + st[1:].lower()
    spaces = (whole.split())
    finale = " "
    finale = finale.join(spaces)
    return finale