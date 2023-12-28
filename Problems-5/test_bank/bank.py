def main():
    text = input("Greeting: ")
    print("$",value(text),sep = "")


def value(greeting):
    promises = 0
    if "HELLO" in greeting.upper()[0:5]:
        promises += 0
    elif "H" in greeting.upper()[0]:
        promises += 20
    else:
        promises += 100
    return promises


if __name__ == "__main__":
    main()
