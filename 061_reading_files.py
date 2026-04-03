# TXT
file_path = "example1.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)

# JSON
print()
import json

file_path = "example1.json"
with open(file_path, "r") as file:
    content = json.load(file)
    print(content)
    print(content["age"])

# CSV
print()
import csv

file_path = "example1.csv"
with open(file_path, "r") as file:
    content = csv.reader(file)
    for row in content:
        print(row)