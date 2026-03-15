# indexing:
# accessing elements of a sequence using [] (indexing operator)
# [start:end:step]

number = "1234-5678-9101"

print(number[0])
print(number[0:4]) # end is exclusive
print(number[5:9])
print(number[5:]) # 5 till end
print(number[:4]) # 0 to 4
print(number[-1]) # reverse indexing
print(number[::2])