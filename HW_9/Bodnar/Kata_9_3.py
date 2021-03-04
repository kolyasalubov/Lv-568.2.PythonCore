class Human:
    def __init__(self):
        pass
class Man(Human):
    def __init__(self):
        super().__init__()
        name1 = "Adam"
        self.name1 = name1
class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__()
        self.name = name
def God():
    m = Man()
    w = Woman()
    return [m,w]