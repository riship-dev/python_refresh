# logical operators:
# or: at least one condition true
# and: both conditions must be true
# not: invert the condition

temp = 29
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("Event cancelled")
else:
    print("Event scheduled")

if temp >= 28 and is_sunny:
    print("It is hot")
else:
    print("Not hot")

if not is_sunny:
    print("It is not sunny")