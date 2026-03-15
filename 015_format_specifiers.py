x = 42
pi = 3.14159

print(f"{x:d}")        # prints x as a decimal (base 10) integer
print(f"{x:b}")        # prints x in binary (base 2)
print(f"{x:o}")        # prints x in octal (base 8)
print(f"{x:x}")        # prints x in hexadecimal (base 16, lowercase)
print(f"{pi:.2f}")     # prints pi as a floating-point number with 2 decimal places
print(f"{1000000:,}")  # prints number with a thousands separator (1,000,000)
print(f"{0.75:.2%}")   # converts number to percentage with 2 decimal places (75.00%)