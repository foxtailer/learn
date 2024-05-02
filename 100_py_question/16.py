# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81


def unswer(n:tuple):
  """
  >>> unswer((1,2,3,4,5,6,7,8,9))
  1,9,25,49,81
  """
  print(*(element*element for element in n if element % 2), sep=",")




if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
  
  user_input = ((1,2,3,4,5,6,7,8,9))
  result = unswer(user_input)
