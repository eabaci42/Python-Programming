# Consolidated file for the category: functions
# This file contains the following original files:
# - cat11.py
# - mario2.py
# - mario3.py
# - mario4.py
# - mario5.py
# - mario6.py
# - mario7.py

################################################################################

# Demonstrates defining functions


def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()


# Prints column of bricks using a function with a loop


def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")


main()


# Prints column of bricks using a function with str multiplication


def main():
    print_column(3)


def print_column(height):
    print("#\n" * height, end="")


main()


# Prints row of coins using a function with str multiplication


def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()


# Prints square of bricks using a function with nested loops


def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()


# Prints square of bricks using a function with a loop and str multiplication


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print("#" * size)


main()


# Prints square of bricks using a function with a loop and str multiplication


def main():
    print_square(3)


def print_square(size):
    for _ in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()


