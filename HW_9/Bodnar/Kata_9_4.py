class Person:
    def __init__(self,name = str, age = int):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
    def getInfo(self):
        print(f"{self.name}s age is {self.age}")
