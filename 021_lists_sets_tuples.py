# collection: single "variable" used to store multiple values
# list: [] ordered and changeable; Duplicates ok
# set: {} unordered and immutable; but add/ remove ok; no duplicates
# tuple: () ordered and unchangeable; duplicates ok; faster

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits[2])
print(fruits[1:3])
print(fruits[::-1]) # prints result in reverse

for fruit in fruits:
    print(fruit, end=" ")
print()

print(len(fruits))

print("apple" in fruits) # in operator returns boolean

fruits.append("pineapple") # appends to end of list
print(fruits)

fruits.pop() # pops and returns last element
print(fruits)

fruits.remove("apple") # removes given element from list if exists
print(fruits)

fruits.insert(0, "apple") # inserts given value at given index
print(fruits)

fruits.sort() # sorts in ascending order
print(fruits)

fruits.reverse() # reverses a list
print(fruits)

fruits.clear() # empties list
print(fruits)
fruits = ["apple", "orange", "banana", "coconut"]

print(fruits.index("apple")) # returns index of given element

print(fruits.count("apple")) # returns occurrence of given element

# SETS
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)
print(len(fruits))
print("apple" in fruits)
# print(fruits[0]) # error
fruits.remove("apple")
fruits.pop() # randomly pops
fruits.clear()

# TUPLES
fruits = ("apple", "orange", "banana", "coconut")
print(fruits.count())
print(fruits[2])
fruits.index("apple")
for fruit in fruits:
    print(fruit)