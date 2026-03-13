# typecasting: the process of converting a variable from one data type to another; str(), int(), float(), bool()

name = "Rishi"
age = 23
gpa = 9.1
is_student = True

print(type(name)) # get data type

gpa = int(gpa) # convert data type; truncates decimal portion; no rounding
print(gpa)

age = str(age)
print(age)
print(type(age))