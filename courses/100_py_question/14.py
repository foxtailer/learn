# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

def unswer(s:str):
  """
  >>> unswer("D g")
  UPPER = 1
  LOWER = 1
  """
  UPPER = 0
  LOWER = 0

  for i in s:
    if i.isalpha():
      if i.isupper():
        UPPER += 1
      else:
        LOWER += 1
  
  print(f"{UPPER = }\n{LOWER = }")


if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
  
  user_input = "gg F!"
  unswer(user_input)
