'''
keyword arguments:
an argument preceded by an identifier
helps with readability
order of arguments does not matter
'''

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello(greeting="hello", title="Mr.", first="John", last="Doe")