'''
list comprehension:
a concise way to create lists in python
compact and easier to read than traditional loops
[expression for value in iterable if condition]
'''

numbers = [x for x in range(1, 11) if x % 2 == 0]
print(numbers)