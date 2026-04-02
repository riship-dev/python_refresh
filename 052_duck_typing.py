'''
duck typing:
another way to achieve polymorphism besides inheritance
object must have minimum necessary attributes/methods
"If it looks like a duck and quacks like a duck, it must be a duck"
'''

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car: # looks like an animal and speaks like an animal, it must be an animal
    is_alive = False
    def speak(self):
        print("HONK")

objects = [Dog(), Cat(), Car()]
for object in objects:
    print(object.is_alive)
    object.speak()
    print()