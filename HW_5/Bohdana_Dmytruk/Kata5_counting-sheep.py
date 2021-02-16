def count_sheeps(sheep):
  # TODO May the force be with you
    sheep_number=0
    for i in sheep:
        if i==True:
            sheep_number+=1
        else:
            continue
    return sheep_number