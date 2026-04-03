'''
decorator:
A function that extends the behavior of another function without modifying the base function
pass the base function as an argument to the decorator

@add_sprinkles
get_ice_cream("vanilla")
'''

def add_sprinkles(base_function):
    def wrapper():
        print("*sprinkles*")
        base_function()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("ice cream")

get_ice_cream()