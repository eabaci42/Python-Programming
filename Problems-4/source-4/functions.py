# Consolidated file for the category: functions
# This file contains the following original files:
# - sayings0.py
# - sayings1.py
# - sayings2.py

################################################################################

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# Doesn't check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


main()


# Check __name__


def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()


