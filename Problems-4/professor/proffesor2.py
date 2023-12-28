import random
import sys


def main():
    score = 0
    while True:
        try:
            level = get_level()
            break
        except ValueError:
            pass
    while True:
        num_one, num_two = generate_integer(level)
        check = True
        while check:
            try:
                total = int(input(f"{num_one} + {num_two} = "))
                if total == (num_one + num_two):
                    check = False
                    score += 1
                else:
                    print("EEE")
            except ValueError:
                pass
            except EOFError:
                sys.exit(f"\nScore: {score}")


def get_level():
    level = int(input("Level: "))
    if 1 <= level <= 3:
        return level
    return "false"


def generate_integer(level):
    if level == 1:
        num_one = random.randint(0, 9)
        num_two = random.randint(0, 9)
    elif level == 2:
        num_one = random.randint(0, 99)
        num_two = random.randint(0, 99)
    else:
        num_one = random.randint(0, 999)
        num_two = random.randint(0, 999)
    return num_one, num_two


if __name__ == "__main__":
    main()
