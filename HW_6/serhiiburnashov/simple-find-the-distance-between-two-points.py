def distance(x1, y1, x2, y2):
    """Given two ordered pairs calculate the distance between them."""

    distance_between_two_points = (((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))) ** 0.5
    return round(distance_between_two_points, 2)


print(distance(1, 1, 0, 0))
