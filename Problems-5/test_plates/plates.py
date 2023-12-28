def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    if not 2 <= len(s) <= 6 or not s.isalnum():
        return False
    for c in s[:2]:
        if not c.isalpha():
            return False
    i = 2
    while i < len(s):
        if s[i].isdigit():
            if s[i + 1 :].isalpha():
                return False
        if s[2:i] == "0":
            return False
        i += 1
    return True


if __name__ == "__main__":
    main()
