def zero_fuel(distance_to_pump, mpg, fuel_left):
    s = mpg * fuel_left
    if s >= distance_to_pump:
        return True
    else:
        return False