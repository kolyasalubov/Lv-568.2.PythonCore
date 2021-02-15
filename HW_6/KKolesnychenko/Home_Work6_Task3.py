def number_characters(text):
    """The function that return the number of characters in the string
    Args:
        text ([str]): text
    """
    text=''.join(text.split())
    for i in set(text):
        print(i,text.count(i))

number_characters("hello world hello")