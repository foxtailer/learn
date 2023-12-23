class A:
    public = 123
    _protected = 123
    __private = 123

a = A()

print(a._A__private)
a._A__private = 22
print(a._A__private)

print(A.__dict__)