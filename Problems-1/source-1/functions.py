# Consolidated file for the category: functions
# This file contains the following original files:
# - parity1.py
# - parity2.py
# - parity3.py

################################################################################

# Demonstrates a function that returns a bool


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()


# Demonstrates conditional expressions (ternary operators)


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()


# Demonstrates returning the value of a Boolean expression


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()


