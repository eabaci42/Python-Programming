# Consolidated file for the category: miscellaneous
# This file contains the following original files:
# - cat0.py
# - cat1.py
# - cat10.py
# - cat2.py
# - cat3.py
# - cat4.py
# - cat5.py
# - cat6.py
# - cat7.py
# - cat8.py
# - cat9.py
# - hogwarts0.py
# - hogwarts1.py
# - hogwarts2.py
# - hogwarts3.py
# - hogwarts4.py
# - hogwarts5.py
# - mario0.py
# - mario1.py

################################################################################

# Demonstrates multiple (identical) function calls

print("meow")
print("meow")
print("meow")


# Demonstrates a while loop, counting down

i = 3
while i != 0:
    print("meow")
    i = i - 1


# Removes continue

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# Demonstrates a while loop, counting up from 1

i = 1
while i <= 3:
    print("meow")
    i = i + 1


# Demonstrates a while loop, counting up from 0

i = 0
while i < 3:
    print("meow")
    i = i + 1


# Demonstrates (more succinct) incrementation

i = 0
while i < 3:
    print("meow")
    i += 1


# Demonstrates a for loop, using a list

for i in [0, 1, 2]:
    print("meow")


# Demonstrates a for loop, using range

for i in range(3):
    print("meow")


# Demonstrates a for loop, with _ as a variable

for _ in range(3):
    print("meow")


# Demonstrates str multiplication

print("meow\n" * 3, end="")


# Introduces continue, break

while True:
    n = int(input("What's n? "))
    if n <= 0:
        continue
    else:
        break

for _ in range(n):
    print("meow")


# Demonstrates indexing into a list

students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])


# Demonstrates iterating over a list

students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)


# Demonstrates iterating over and indexing into a list

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])


# Demonstrates indexing into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# Demonstrates iterating over and index into a dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")


# Demonstrates iterating over a list of dict objects

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# Prints a column of bricks

print("#")
print("#")
print("#")


# Prints column of bricks using a loop

for _ in range(3):
    print("#")


