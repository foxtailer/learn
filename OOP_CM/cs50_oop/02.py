class Student():
    def __init__(self, name, home, patronus):
        if not name:
            raise ValueError('Missing name')
        if home not in ['Gryffindor', 'Hufflepuff', 'Ravenclaww', 'Slytherin']:
            raise ValueError('Invalid home')
        self.name = name
        self.home = home
        self.patronus = patronus
    
    def __str__(self):
        return f'{self.name} from {self.home}'
    
    def spell(self):
        match self.patronus:
            case 'dog':
                print('dog')
            case 'cat':
                print('cat')
            case _:
                print('0')


def main():
    student = Student('hari', 'Hufflepuff', 'buum')
    print(f'student {student.name} from {student.home}')
    print(student)
    student.spell()


if __name__ == '__main__':
    main()