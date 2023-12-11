# object method
class Person:
    name: str

    def __init__(self, name) -> None:
        self.name = name
    
    def say_hay(self):
        print(f"Hello, my name is {self.name}")

p = Person("Ivan")
p.say_hay()
print()

# class method
class Person2:
    workplase = "Something"

    @classmethod
    def get_workplase(cls):
        print(cls.workplase)

p2 = Person2()
Person2.get_workplase()
p2.get_workplase()

