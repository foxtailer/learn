# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Dog():

    def __init__(self, color, age):
        self.color = color
        self.age = age

    def burk(self):
        print('Grrrr')

bobik = Dog('black', 1)
print(bobik.age)
bobik.burk()


class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = IOstring()
xx.get_string()
xx.print_string()