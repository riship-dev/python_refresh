x = 10
x = x + 1
x += 1 # augmented assignment operator
print(x)

x = x - 1
x -= 1
print(x)

x = x * 3
x *= 3
print(x)

x = x / 3 # returns float
x /= 3
print(x)

x = x ** 2
x **= 2
print(x)

x = x % 3
x %= 3
print(x)

x = 3.14
y = -4
z = 5
print(round(x)) # rounds to nearest whole number
print(abs(y)) # absolute value wrt zero
print(pow(y, 2)) # power
print(max(x, y, z)) # returns maximum value
print(min(x, y, z)) # returns minimum value

import math

print(math.pi) 
print(math.e) # exponential constant
print(math.sqrt(25)) # square root
print(math.ceil(8.1)) # rounds up to nearest whole number
print(math.floor(9.9)) # rounds down to nearest whole number