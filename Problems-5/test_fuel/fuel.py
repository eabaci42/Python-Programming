def main():
    # Main function to get user input and display gauge reading
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    # Convert a fraction to a percentage
    try:
        # Split the fraction into numerator and denominator
        numbers = fraction.split("/")
        if len(numbers) != 2:
            # Raise ValueError if the input is not a fraction
            raise ValueError
        # Convert the parts of the fraction to integers
        x, y = int(numbers[0]), int(numbers[1])
        # Return the fraction as a percentage
        return int(round((x / y) * 100))

    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError


def gauge(percentage):
    # Determine the fuel gauge reading based on the percentage
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
