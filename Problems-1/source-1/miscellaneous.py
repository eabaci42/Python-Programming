# Consolidated file for the category: miscellaneous
# This file contains the following original files:
# - agree0.py
# - agree1.py
# - agree2.py
# - agree3.py
# - agree4.py
# - compare0.py
# - compare1.py
# - compare2.py
# - compare3.py
# - compare4.py
# - compare5.py
# - grade0.py
# - grade1.py
# - grade2.py
# - grade3.py
# - house0.py
# - house1.py
# - house2.py
# - house3.py
# - parity0.py

################################################################################

# Compares strings

answer = input("Do you agree? ")
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")


# Strips string before comparing

answer = input("Do you agree? ").strip()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")


# Lowercases string before comparing

answer = input("Do you agree? ").strip().lower()
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")


# Compares multiple strings

answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Agreed")
else:
    print("Not agreed")


# Compares multiple strings

answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not agreed")


# Demonstrates conditionals

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


# Demonstrates mutually exclusive conditions

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")


# Demonstrates fewer conditions

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


# Demonstrates inequalities and logical operator

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# Demonstrates equality

x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")


# Demonstrates inequality

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


# Demonstrates inequalities and logical operators

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")


# Demonstrates inequalities and logical operators

score = int(input("Score: "))

if 90 <= score and score <= 100:
    print("Grade: A")
elif 80 <= score and score < 90:
    print("Grade: B")
elif 70 <= score and score < 80:
    print("Grade: C")
elif 60 <= score and score < 70:
    print("Grade: D")
else:
    print("Grade: F")


# Demonstrates chained comparisons

score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")


# Demonstrates fewer comparisons

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# Compares multiple strings with if/elif/else

name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# Uses or

name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


# Uses match with case

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Uses |

name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")


# Demonstrates modulo operator

x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


