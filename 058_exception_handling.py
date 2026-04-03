'''
exception:
an event that interrupts the flow of the program
[ZeroDivisionError, TypeError, ValueError]
try:
    try some code 
except Exception:
    handle exception
finally:
    do some clean up
'''

try:
    number = int(input("Number?: "))
    print(1 / number)
except ZeroDivisionError:
    print("zero error")
except ValueError:
    print("value error")
except Exception:
    print("other error")
finally:
    print("cleanup")