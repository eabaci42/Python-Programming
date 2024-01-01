# Consolidated file for the category: miscellaneous
# This file contains the following original files:
# - hello1.py
# - calculator0.py
# - hello5.py
# - calculator4.py
# - hello4.py
# - calculator5.py
# - hello0.py
# - calculator1.py
# - hello7.py
# - calculator6.py
# - hello3.py
# - calculator2.py
# - calculator10.py
# - hello2.py
# - calculator3.py
# - hello6.py
# - calculator7.py
# - calculator8.py
# - calculator9.py

################################################################################

# Demonstrates a function with a positional argument and a return value

name = input("What's your name? ")
print("hello,")
print(name)


# Demonstrates addition

x = 1
y = 2

z = x + y

print(z)


# Demonstrates a format string

name = input("What's your name? ")
print(f"hello, {name}")


# Demonstrates conversion of str to float

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(z)


# Demonstrates a function with a positional argument and a named argument

name = input("What's your name? ")
print("hello, ", end="")
print(name)


# Demonstrates rounding to nearest int

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)


# Demonstrates a function with a positional argument

print("hello, world")


# Demonstrates (unintended) concatenation of strings

# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z)


# Demonstrates str functions

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")


# Demonstrates fewer variables

x = float(input("What's x? "))
y = float(input("What's y? "))

print(round(x + y))


# Demonstrates a function with two positional arguments

name = input("What's your name? ")
print("hello,", name)


# Demonstrates conversion from str to int

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)


# Demonstrates formatting after the decimal place

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.2f}")


# Demonstrates concatenation of strings

name = input("What's your name? ")
print("hello, " + name)


# Demonstrates nesting of function calls

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(z)


# Demonstrates str functions

name = input("What's your name? ").strip().title()
print(f"hello, {name}")


# Demonstrates formatting with commas

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")


# Demonstrates division

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)


# Demonstrates rounding after the decimal point

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)


