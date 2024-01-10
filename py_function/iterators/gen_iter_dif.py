# iterator
nums = [1, 2, 3, 4]
obj = iter(nums)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# generator
def nums():
   for i in range(1, 5):
       yield i
obj = nums()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# iterator
class Alphabets:
  def __iter__(self):
      self.val = 65
      return self
  def __next__(self):
      if self.val > 90:
          raise StopIteration
      temp = self.val
      self.val += 1
      return chr(temp)
my_letters = Alphabets()
my_iterator = iter(my_letters)
for letter in my_iterator:
   print(letter, end = " ")

# generator
def Alphabets():
   for i in range(65, 91):
       yield chr(i)
my_letters = Alphabets()
for letter in my_letters:
   print(letter, end=" ")

def gener():
   List = ["orange", "green", "black"]
   for item in List:
       yield item
iter_obj = gener()
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

# iterator
List = ["orange", "green", "black"]
list_iter = iter(List)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))

class Multiples:
  def __iter__(self):
      self.val = 1
      return self
  def __next__(self):
      temp = self.val
      self.val += 1
      return temp*5
multiples5 = Multiples()
obj = iter(multiples5)
print(next(obj))
print(next(obj))
print(next(obj))

# generator
def Multiples():
   i = 1
   while True:
       yield i*5
       i += 1
multiples5 = Multiples()
obj = multiples5
print(next(obj))
print(next(obj))
print(next(obj))

"""
Iterators in Python	                                          Generators in Python

Implemented using Class	                                      Implemented using Function
No yield statement	                                          Use yield statement
Use the iter() function	                                      Do not use the iter() function.
Local variables are not used	                              Local variables are used
They are mostly used to convert iterables into iterators	  They are mostly used to create iterators
All iterators are not generators	                          All generators are iterators
"""