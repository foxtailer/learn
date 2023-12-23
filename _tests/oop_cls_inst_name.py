class A:
    name = 1
    def __init__(self, name) -> None:
        self.name = name

a = A(2)

print(a.name)
print(A.name)