class CustomError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(f"My repr: {self.data}")



def age_chekin (age):
    try:
        if age%2==0:
            print(f'{age} is even')
        else:
            print(f'{age} is odd')
        if age<=0:
            raise CustomError('your age shoud be positive')
    except CustomError as e:
        print('Error:', e.data)
    else:
        print("welcome")


m = int(input('your age? - '))
age_chekin(m)


