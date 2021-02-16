def count_symbols (word):
  """This function calculates all symbols in string"""
  
  letter_dict = {}
  for letter in word:
    if letter not in letter_dict:
      letter_dict[letter] = 1
    else:
      letter_dict[letter] = letter_dict[letter]+1
  return letter_dict


print(count_symbols(input("Please, enter your string: ")))