'''
variable scope: where a variable is visible and accessible
scope resolution: LEGB local->enclosed->global->built-in 
'''

# local
def func1():
    a = 1
    print(a) # a accessible only in func1

def func2():
    b = 1
    print(b) # b accessible only in func2

# enclosed
def func1():
    x = 1
    def func2():
        #x = 2
        print(x)
    func2()

func1()

# global
x = 3
def func3():
    print(x)
def func4():
    print(x)
func3()
func4()

# built-in

from math import e

def func6():
    print(e)

func6()
e = 3

func6()