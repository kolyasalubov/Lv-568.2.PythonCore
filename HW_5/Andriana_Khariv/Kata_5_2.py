def enough(cap, on, wait):
    a = cap - on
    while a >= wait:
        return 0
    else:
        return wait - a
