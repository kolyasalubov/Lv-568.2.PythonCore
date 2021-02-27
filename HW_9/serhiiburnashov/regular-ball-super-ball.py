class Ball(object):
    """ Some text explaining the class. """

    def __init__(self, ball_type="regular"):
        """ Some text explaining the function. """

        self.ball_type = ball_type


# "regular"
print(Ball().ball_type)
# "super"
print(Ball("super").ball_type)
