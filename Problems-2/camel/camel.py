# camelCase
# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

def main():
    camelcase = input("camelCase: ")
    convert_snake_case(camelcase)

# Print method
def convert_snake_case(name):
    print("snake_case: ", end="")
    for char in name:
        if char.isupper():
            print("_" + char.lower(), end="")
            continue
        print(char, end="")
    print()

main()

# Alternative Solve
# New string create method
# def main():
#     camel_case = input("camelCase: ")
#     snake_case = convert_to_snake_case(camel_case)
#     print("snake_case:", snake_case)

# def convert_to_snake_case(name):
#     snake_case_name = ""
#     for char in name:
#         if char.isupper():
#             snake_case_name += "_" + char.lower()
#         else:
#             snake_case_name += char
#     return snake_case_name

# main()
