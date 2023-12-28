import random


def main():
    score = 0
    level = get_level()
    ten = 10
    while ten > 0:
        num_one, num_two = generate_integer(level)
        wrong = 0
        while True:
            if wrong != 3:
                try:
                    total = int(input(f"{num_one} + {num_two} = "))
                    if total == (num_one + num_two):
                        score += 1
                        ten -= 1
                        break
                    else:
                        print("EEE")
                        wrong += 1
                except ValueError:
                    pass
                except EOFError:
                    ten = 0
                    print(f"\nScore: {score}")
            else:
                total = num_one + num_two
                print(f"{num_one} + {num_two} = {total}")
                ten -= 1
                break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        num_one = random.randint(0, 9)
        num_two = random.randint(0, 9)
    elif level == 2:
        num_one = random.randint(10, 99)
        num_two = random.randint(10, 99)
    else:
        num_one = random.randint(100, 999)
        num_two = random.randint(100, 999)
    return num_one, num_two


if __name__ == "__main__":
    main()
