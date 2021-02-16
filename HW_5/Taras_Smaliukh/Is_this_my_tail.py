def correct_tail(body, tail):
#      sub = body.substr(len(body)-len(tail.length)
        if body[-1] == tail:
            return True
        else:
            return False