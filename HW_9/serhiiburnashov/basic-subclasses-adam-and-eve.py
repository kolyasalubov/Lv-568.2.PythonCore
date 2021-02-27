def God():
    """ Some text explaining the function. """

    Adam = Man()
    Eve = Woman()
    result = [Adam, Eve]
    return result


class Human:
    """ Some text explaining the class. """
    
    pass


class Man(Human):
    """ Some text explaining the class. """

    pass


class Woman(Human):
    """ Some text explaining the class. """

    pass


paradise = God()
print(isinstance(paradise[0], Man), True, "First object are a man")
