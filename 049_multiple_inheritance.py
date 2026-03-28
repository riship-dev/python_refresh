'''
multiple inheritance:
inherit from more than one parent class
C(A, B)

multilevel inheritance:
inherit from a parent which inherits from another parent
C(B) <- B(A) <- A
'''

class Animal:
    def eat(self):
        print("eating")

class Prey(Animal):
    def flee(self):
        print("flee")

class Predator(Animal):
    def hunt(self):
        print("hunting")

class Fish(Prey, Predator):
    pass

fish1 = Fish()
fish1.flee()
fish1.hunt()
fish1.eat()