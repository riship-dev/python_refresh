'''
multi-threading:
used to perform tasks concurrently (multitasking)
good for i/o bound tasks like reading files or fetching data from APIs
threading.Thread(target=my_function)
'''

import threading
import time

def walk_dog():
    time.sleep(8)
    print("walk the dog")

def take_out_trash():
    time.sleep(2)
    print("take out trash")

def get_mail():
    time.sleep(4)
    print("you get the mail")

thread1 = threading.Thread(target=walk_dog) # (target=walk_dog, args=(a, b, c)) for functions with arguments
thread1.start()

thread2 = threading.Thread(target=take_out_trash)
thread2.start()

thread3 = threading.Thread(target=get_mail)
thread3.start()

# wait for threads to finish before continuing the program
thread1.join()
thread2.join()
thread3.join()

print("Hello")