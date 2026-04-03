# python writing files [.txt, .json, .csv]

# TXT
text_data = "Hello World"
file_path = "example1.txt" # relative to project root

with open(file_path, "w") as file: # "w" overwrites existing file
    file.write("")
    print(f"Text file {file_path} created")
with open(file_path, "a") as file: # "a" writes at end of file
    file.write(f"{text_data}")
    print(f"Writing on {file_path}")

# JSON
print()
import json

employee = {
    "name": "john doe",
    "age": 30,
    "job": "cook"
}
file_path = "example1.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent=4)
    print(f"JSON file created at {file_path}")

# CSV
print()
import csv

file_path = "example1.csv"
employees = [
    ["Name", "Age", "Job"],
    ["John Doe", 23, "Cook"],
    ["Jane Smith", 34, "Cashier"],
    ["First Last", 99, "Chef"],
]

with open(file_path, "w", newline="") as file: # default new line = \n
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file {file_path} created")