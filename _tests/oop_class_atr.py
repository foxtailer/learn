class A:
    name = "cls"

    def __init__(self, age) -> None:
        self.age = age

x = A(30)
y = A(30)

print(x.name, y.name)

A.name = "pms"

print(x.name, y.name)
        