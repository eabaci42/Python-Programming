# I’m thinking of a number between 1 and 100…

# In a file called game.py, implement a program that:

# Prompts the user for a level,
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
import random
import sys


def main():
    control()


def control():
    while True:
        try:
            level = int(get_in("level"))
            if 0 < level:
                break
        except ValueError:
            pass

    number = random.randint(1, level)
    while True:
        try:
            guess = int(get_in("guess:"))
            if 0 < guess:
                get_out(guess, number)
        except ValueError:
            pass


def get_in(set):
    if set == "level":
        number = input("Level: ")
    else:
        number = input("Guess: ")
    return number


def get_out(guess, number):
    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        sys.exit("Just right!")


if __name__ == "__main__":
    main()
