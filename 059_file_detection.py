# python file detection

import os

file_path = "059_file_detection.py" # D:/software_development/python_refresh/059_file_detection.py

if os.path.exists(file_path):
    print(f"file path {file_path} exists")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory")
else:
    print("Location does not exist")