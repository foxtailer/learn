class Student:
    students = []
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Student.students.append(self)

    def get_info(self):
        return f'{self.name.capitalize()} {self.age}'
    
    @classmethod
    def _clear(cls):
        # for i in cls.students:   # Deleate i variable thar refer to students[i]
        #     del i

        Student.students.clear()


student1 = Student('name', 20)
student2 = Student('name', 20)

print(student1.get_info())
print(student1 is Student.students[0])

Student._clear()
print(student1.get_info())
print(Student.students[0])
print(Student.students[0].get_info())
