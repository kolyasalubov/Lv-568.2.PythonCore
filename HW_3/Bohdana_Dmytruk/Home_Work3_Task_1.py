zen_of_python = (r"""    Beautiful is better than ugly.
    Explicit is better than implicit. 
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.      
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!""")

print("Text in upper case:", 
    zen_of_python.upper()) 

print("Text after replacing letter 'i' into '&':",
    zen_of_python.replace("i", "&"))
 
list_of_words = zen_of_python.split()
print("Count of words 'better' is: ", list_of_words.count("better"))
print("Count of words 'never' is: ", list_of_words.count("never")+list_of_words.count("never."))
print("Count of words 'is' is: ", list_of_words.count("is"))