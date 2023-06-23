class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f'{self.name} {self.house}'
    
    
    @classmethod
    def get(cls):
        name = input('Name: ')
        house = input('House: ')
        return cls(name, house)
    
student = Student.get()
print(student)