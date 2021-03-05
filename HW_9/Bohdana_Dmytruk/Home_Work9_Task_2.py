days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday',
         5:'Friday', 6:'Saturday', 7:'Sunday'}

try:
    key = int(input('Enter number that repersents the day of the week: '))
    dat = days.get(key)
    if dat != None:
        print(dat)
    else:
        raise Exception
except ValueError:
    print('You should enter number')
except Exception:
    print('There is no day to represent that number')

