def correct_tail(body, tail):
    """
    If the tail is right return true, else return false.
    """
    
    sub = body[len(body)-len(tail)]
    message = True if sub == tail else False
    return message


#True
print(correct_tail("Fox", "x"))
#True
print(correct_tail("Rhino", "o"))
#True
print(correct_tail("Meerkat", "t"))
#False
print(correct_tail("Emu", "t"))
#False
print(correct_tail("Badger", "s"))
#False
print(correct_tail("Giraffe", "d"))
        