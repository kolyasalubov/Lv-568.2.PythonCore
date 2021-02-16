def enough(cap, on, wait):
    # Your code here
    if on + wait <= cap:
        return int('0')
    else:
        return (on + wait - cap)