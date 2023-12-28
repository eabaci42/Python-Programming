# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def main():
    fraction = validate_fraction()
    fuel_level(fraction)


def validate_fraction():
    while True:
        fraction = get_fraction()
        if "/" in fraction:
            x, fraction = validate_x(fraction)
            y = validate_y(x, fraction)
            if x / y <= 1:
                return x / y


def get_fraction():
    return input("Fraction: ")


def varible_x(fraction):
    x = ""
    for slash in fraction:
        if slash == "/":
            return x
        x += slash


def validate_x(fraction):
    while True:
        try:
            return int(varible_x(fraction)), fraction
        except ValueError:
            fraction = get_fraction()


def varible_y(x, fraction):
    x = str(x) + "/"
    return int(fraction.replace(x, ""))


def validate_y(x, fraction):
    while True:
        try:
            y = int(varible_y(x, fraction))
            x / y
            return y
        except ValueError:
            fraction = get_fraction()
        except ZeroDivisionError:
            fraction = get_fraction()


def fuel_level(level):
    if 0 / 100 <= level <= 1 / 100:
        print("E")
    elif 99 / 100 <= level <= 100 / 100:
        print("F")
    else:
        level = int(round(level, 2) * 100)
        print(str(level) + "%")


main()
