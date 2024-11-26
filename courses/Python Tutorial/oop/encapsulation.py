""" Encapsulation - wrapping data inside container
by create a private variable we restrict the acess to
data. only using class metods we can modify class variabels"""
class Test():
  def __init__(self):
    self.__value = 5  # Private attributes

  def __del__(self):
    print("*")

a = Test()
a.value = 4
print(a.value)