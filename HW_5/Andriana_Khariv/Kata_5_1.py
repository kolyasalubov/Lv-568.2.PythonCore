def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = distance_to_pump / mpg
    while a <= fuel_left:
        return True
    else:
        return False
