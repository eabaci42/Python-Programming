# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len_two_letters(s):
        if whitespace(s):
            if middle(s):
                if zerodec(s):
                    return True
    return False

def len_two_letters(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            return True
        else:
            return False

def whitespace(s):
    if s.isalnum():
        return True
    else:
        return False

def middle(s):
    l = len(s)
    while 3 <= l:
        if s[l-1].isalpha():
            if s[l-2].isdigit():
                return False
        l -= 1
    return True

def zerodec(s):
    l = len(s)-1
    i = 2
    while i <= l:
        if s[i] in "123456789":
            if i != l:
                if s[i+1] == "0":
                    return True
            else:
                break
        elif s[i] == "0":
            if i != l:
                if s[i+1].isdigit() or s[i+1].isalpha():
                    return False
            else:
                if s[i] == "0":
                    return False
        i += 1
    return True

main()

