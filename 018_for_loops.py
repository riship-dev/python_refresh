# for loops:
# execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc.

for x in range(1, 11): # 11 is exclusive
    print(x, end=" ")

print()
number = "123456789"
for x in number:
    print(x, end=" ")

print()
for x in number:
    if x == "3":
        continue # skips current iteration
    print(x, end=" ")

print()
for x in number:
    if x == "3":
        break # exits loop
    print(x, end=" ")