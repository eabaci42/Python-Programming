# Consolidated file for the category: functions
# This file contains the following original files:
# - hello10.py
# - hello11.py
# - calculator11.py
# - hello9.py
# - hello8.py

################################################################################

# Demonstrates defining a function with a parameter with a default value


def hello(to="world"):
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)


# Demonstrates defining a main function


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()


# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()


# Demonstrates defining a function with a parameter


def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)


# Demonstrates defining a function without parameters


def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)


