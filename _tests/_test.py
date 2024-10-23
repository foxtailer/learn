class A:
    def fun(self):
        print('A')

class B(A):
    pass

class C(A):
    def fun(self):
        print('C')

class D(B, C):
    pass

d = D()

d.fun()