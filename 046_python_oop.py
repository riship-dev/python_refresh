'''
object:
a bundle of attributes and methods
need class to create many objects

class: used to design the structure and layout of object
'''

class Car:
    def __init__(self, make, year, colour, for_sale):
        self.make = make
        self.year = year
        self.colour = colour
        self.for_sale = for_sale
    
    def drive(self):
        print(f"{self.make} moving") 

car1 = Car("bmw", 2023, "red", True)

print(car1.make)
car1.drive()