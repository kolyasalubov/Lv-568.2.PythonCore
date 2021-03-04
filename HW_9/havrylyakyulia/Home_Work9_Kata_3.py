class Human:
    pass    
    
class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    Adam = Man()
    Eve = Woman()
    res_1 = Adam
    res_2 = Eve
    return res_1, res_2