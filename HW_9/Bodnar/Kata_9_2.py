class Ghost:
    def __init__(self):
        import random
        list_col = ["red", "white", "yellow", "purple"]
        color = random.choice(list_col)
        self.color = color