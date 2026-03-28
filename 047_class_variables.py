'''
class variables:
shared among all instances
defined outside the constructor
allow you to share data among all objects from that class
'''

class Student:
    year = 2025
    num = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.num += 1

student1 = Student("John Doe", 34)
student2 = Student("Patrick", 45)

print(student1.name, student1.age)
print(student2.name, student2.age)
print(student1.year)
print(Student.year)