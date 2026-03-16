fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0])
print(groceries[0][0])

for collection in groceries:
    print(collection)

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()