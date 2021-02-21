def are_you_playing_banjo(name):
    """
    Function which answers the question "Are you playing banjo?".
    """

    сheck = name[0].lower() == "r"
    message = name + " plays banjo" if сheck else name + " does not play banjo"
    return message


#martin does not play banjo
print(are_you_playing_banjo("martin"))
#Rikke plays banjo
print(are_you_playing_banjo("Rikke"))
