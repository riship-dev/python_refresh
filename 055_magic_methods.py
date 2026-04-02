'''
magic methods:
dunder methods (double underscores) __init__, __str__, __eq__
they are automatically called by many of python's in-built operations
they allow developers to define ot customize the behavior of objects
'''

class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    
    def __str__(self):
        return f"name: {self.name}\ngpa: {self.gpa}"
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __gt__(self, other): # greater than; similarly: lt
        return self.gpa > other.gpa
    
    def __add__(self, other):
        return self.gpa + other.gpa
    
    def __contains__(self, keyword):
        return keyword in self.name
    
    def __getitem__(self, key):
        if key == "name":
            return self.name
        elif key == self.gpa:
            return self.gpa
        return -1

student1 = Student("John Doe", 2.3)
student2 = Student("Jane Smith", 2.5)
student3 = Student("John Doe", 9.1)

print(student1) # __str__

# __eq__
print(student1 == student2)
print(student1 == student3)

# __gt__ (greater than)
print(student1 > student2)
print(student3 > student1)

# __add__
print(student1 + student2)

# __contains__
print("John" in student1)
print("Bob" in student1)

# __getitem__
print(student1["name", "gpa"])