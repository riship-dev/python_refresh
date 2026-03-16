# dictionary
# a collection of {key: value} pairs
# ordered and changeable, no duplicates

capitals = {"USA": "Washington D.C.", 
            "India": "New Delhi", 
            "China": "Beijing", 
            "Russia": "Moscow"}

print(capitals.get("USA")) # returns given keys value
print(capitals.get("Japan")) # returns None

capitals.update({"Germany": "Berlin"}) # Appends given key value pair to dictionary
capitals.update({"Germany": "Detroit"}) # Updates given key value pair to dictionary
capitals.pop("China")
capitals.popitem() # removes latest key value pair

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items() # [(), (), ()]
print(items)
for key, values in capitals.items():
    print(f"{key}: {values}")