import random

old_string = input(str("Please input what you would like to change to random caps: "))

def new_string(string):
  result = " "
  for i, character in enumerate(string):
    if i % 2 == 0:
      result += character.upper()
    else:
      result += character.lower()
  return result

print(new_string(old_string))
