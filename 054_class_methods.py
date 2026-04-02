'''
class methods:
allows operations to the class itself
take (cls) as the first parameter, which represents the class itself
'''

class Student:
    count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    # instance method
    def get_info(self):
        return {
            "name": self.name,
            "gpa": self.gpa
        }
    
    @classmethod
    def get_count(cls):
        return cls.count
    
student1 = Student("John Doe 1", 4.5)
student2 = Student("John Doe 2", 3.3)
student3 = Student("John Doe 3", 3.5)

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_count())