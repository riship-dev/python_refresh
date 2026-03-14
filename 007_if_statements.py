# if: do some code only if some condition is True; else do something else

age = int(input())

if age < 0:
    print("Inavlid age")
elif age < 18:
    print("No")
else:
    print("Yes")