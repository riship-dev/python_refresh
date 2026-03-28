'''
Inheritance:
Allows a class to inherit attributes and methods from another class
helps with code reusability and extensibility
class Child(parent)
'''

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog("Scooby")
cat1 = Cat("Garfield")

print(dog1.name)
dog1.eat()