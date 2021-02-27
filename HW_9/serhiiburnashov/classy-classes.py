class Person:
    """ Some text explaining the class. """

    def __init__(self, name, age):
        """ Some text explaining the function. """

        self.info = f"{name}s age is {age}"


names = ["john", "matt", "alex", "cam"]
ages = [16, 25, 57, 39]
for i in range(4):
    name_, age_ = names[i], ages[i]
    person = Person(name_, age_)
    print("Testing for %s and %s" % (repr(name_), age_))
    print(person.info, name_ + "s age is " + str(age_))
