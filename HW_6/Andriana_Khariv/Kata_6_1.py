def distance(x1, y1, x2, y2):
    dist = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (0.5)
    dist = float('{:.2f}'.format(dist))
    return  dist
