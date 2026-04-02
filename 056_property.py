'''
@property:
decorator used to define a method as property (it can be accessed like an attribute)
benefit: add additional logic when read, write, or delete attributes
gives you getter, setter and deleter method
'''

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}"
    
    @property
    def height(self):
        return f"{self._height:.1f}"
    
    @width.getter
    def width(self):
        return self._width
    @height.getter
    def height(self):
        return self._height
    
    @width.setter
    def width(self, new_width):
        self._width = new_width
    @height.setter
    def height(self, new_height):
        self._height = new_height

    @width.deleter
    def width(self):
        del self._width
        print("width deleted")
    @height.deleter
    def height(self):
        del self._height
        print("height deleted")

rectangle = Rectangle(3, 4)

# getters
print(rectangle.width)
print(rectangle.height)
print()

# setters
rectangle.width = 9
rectangle.height = 12
print(rectangle.width)
print(rectangle.height)
print()

# deleter
del rectangle.width
del rectangle.height
#print(rectangle.width)
#print(rectangle.height)
#print()