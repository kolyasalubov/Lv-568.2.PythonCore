list_att = input('enter anything: ')


def number_of_characters():
    for i in list_att:
        print("Character", i, "included",  list_att.count(i), "in a given string", list_att)


number_of_characters()
