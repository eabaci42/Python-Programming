# Consolidated file for the category: miscellaneous
# This file contains the following original files:
# - number0.py
# - number1.py
# - number2.py
# - number3.py
# - number4.py

################################################################################

# Gets a number from the user

x = int(input("What's x? "))
print(f"x is {x}")


# Catches a ValueError

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# Demonstrates a NameError

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")


# Demonstrates else

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# Adds a loop

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


