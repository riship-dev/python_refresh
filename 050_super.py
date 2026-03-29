'''
super:
function used in a child class to call methods from a parent class [superClass]
allows you to extend the functionality of the inherited methods
'''

class Shape:
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled

class Circle(Shape):
    def __init__(self, colour, filled, radius):
        super().__init__(colour, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, colour, filled, width):
        super().__init__(colour, filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, colour, filled, width, height):
        super().__init__(colour, filled)
        self.width = width
        self.height = height

circle = Circle("red", True, 5)
print(circle.colour)
print(circle.radius)