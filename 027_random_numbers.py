import random

die = random.randint(1, 6) # generates whole number; both inclusive
print(die)

print(random.random()) # random float between 0 and 1

options = ("rock", "paper", "scissors")
print(random.choice(options)) # returns random item in collection

cards = [1, 2, 3, 4, 5]
random.shuffle(cards) # shuffles items in collection
print(cards)