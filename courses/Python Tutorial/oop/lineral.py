class A:
  def a(self):
    print("A")

class B:
  def a(self):
    print("B")

class C(B):
  def a(self):
    print("C")

class D(C, A):
  def a(self):
    super().a()
    # super(C, self).a()
    print(self.__class__.__mro__)

D().a()

# Super look for "a" in C -> parent of C(B) -> A -> object class