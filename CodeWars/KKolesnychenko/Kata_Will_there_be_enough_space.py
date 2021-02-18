def enough(cap, on, wait):
    if wait<=cap-on:
        return 0
    else:
        excess=on+wait-cap
        return excess