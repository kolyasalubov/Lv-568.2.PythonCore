def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Function that tells you if it is possible to get to the pump or not."""

    possibility = mpg * fuel_left >= distance_to_pump
    return possibility


#True
print(zero_fuel(50, 25, 2))
#False
print(zero_fuel(100, 50, 1))
