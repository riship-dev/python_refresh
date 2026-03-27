'''
match-case statement (switch):
An alternative to using many "elif" statements
execute some code if a value matches a "case"
benefits: cleaner and syntax is more readable
'''

def day_of_week(day):
    match day:
        case 1:
            return "sunday"
        case 2:
            return "monday"
        case 3:
            return "tuesday"
        case _:
            return "invalid argument"
        
print(day_of_week(2))
print(day_of_week("hi"))