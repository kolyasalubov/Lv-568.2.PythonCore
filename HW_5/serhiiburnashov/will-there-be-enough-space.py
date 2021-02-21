def enough(cap, on, wait):
    """
    If there is enough space, return 0, and if there isn't, 
    return the number of passengers he can't take.
    """

    cant_take = wait - (cap - on)
    return 0 if cant_take < 0 else cant_take


#0
print(enough(10, 5, 5))
#10
print(enough(100, 50, 60))
#-10(0)
print(enough(92, 62, 20))
