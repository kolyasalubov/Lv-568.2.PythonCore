from secrets import choice as random


class Ghost(object):
    """ Some text explaining the class. """

    def __init__(self):
        """ Some text explaining the function. """

        colors = ['white', 'yellow', 'purple', 'red']
        self.color = random(colors)


ghosts = [Ghost().color for _ in range(100)]
print(ghosts)
print(ghosts.count("white"), "white")
print(ghosts.count("yellow"), "yellow")
print(ghosts.count("purple"), "purple")
print(ghosts.count("red"), "red")
