class Person():
    def __init__(self, name, age):
        self.name = str(name) + "s"
        self.age = int(age)
        self.info = "{0} age is {1}" .format(self.name, self.age)
