name = input("Name?: ")

print(len(name))
print(name.find("s")) # first occurrence of a given character; -1 if not found
print(name.rfind("s")) # last occurrence of a given character; -1 if not found
print(name.capitalize()) # returns string capitalized
print(name.upper()) # returns string upper cased
print(name.lower()) # returns string lower cased
print(name.isdigit()) # returns True if string is all digits
print(name.isalpha()) # returns True if string is all alphabetical
print(name.count("i")) # returns count of given character(s) in string
print(name.replace("i", "z")) # returns string with characters replaced