'''
polymorphism:
greek word that means to "have many forms or faces"
poly = many
morphe = form

two ways to achieve polymorphism:
inheritance: an object could be created of the same type as a parent class
"duck typing": object must be necessary attributes/methods
'''

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return self.width * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
shapes = [Square(10), Circle(15), Triangle(10, 20)]

for shape in shapes:
    print(shape.area())