distance_to_pump = int(input("What is the distance to pump? "))
mpg = int(input("How many miles your car takes per gallon? "))
fuel_left = int(input("How many fuel left in your car?'"))

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        return True
    return False
print(zero_fuel(distance_to_pump, mpg, fuel_left))