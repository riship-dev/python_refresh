'''
*args: allows you to pass multiple non-key arguments
**kwargs: allows you to pass multiple keyword-arguments
'''

def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(add(1, 2, 3, 4, 5))

def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(street="king", city="pune", state="MH", pin="54321")