class Human:
    def __init__(self):
        pass
    
class Man(Human):
    def __init__(self):
        Human.__init__(self)
        
class Woman(Human):
    def __init__(self):
        Human.__init__(self)
        
def God():
    Adam = Man()
    Eve = Woman()
    result1 = Adam
    result2 = Eve
    return result1, result2