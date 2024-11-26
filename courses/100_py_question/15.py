# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

def unswer(x:int):
  """
  >>> unswer(9)
  11106
  """
  temp = ['']
  x_str = str(x)
  for i in range(4):
    temp.append(temp[i] + x_str)

  return sum([int(item) for item in temp[1:]])



if __name__ == "__main__":
  import doctest
  doctest.testmod(verbose=True)
  
  user_input = 9
  result = unswer(user_input)
  print(result)
