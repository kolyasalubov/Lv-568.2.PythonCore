def double_char(s):
    """
    Given a string, you have to return a string
    in which each character (case-sensitive) is repeated once.
    """

    result = ''.join(item * 2 for item in s)
    return result


# "SSttrriinngg"
print(double_char("String"))
# "HHeelllloo  WWoorrlldd"
print(double_char("Hello World"))
# "11223344!!__  "
print(double_char("1234!_ "))
