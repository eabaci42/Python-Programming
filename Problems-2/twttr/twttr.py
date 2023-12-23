# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    newstr = ""
    name = input("Input: ")
    for char in name:
        if char == "a" or char == "e" or char == "i" or char == "u" or char == "o":
            newstr += char.replace(char, "")
        elif char == "A" or char == "E" or char == "I" or char == "U" or char == "O":
            newstr += char.replace(char, "")
        else:
            newstr += char
    print("Output:" ,newstr)

main()

# Altarnative
# Usege join and char foe char in name if char not is vowels
# def main():
#     name = input("Input: ")
#     vowels = "aeiouAEIOU"
#     newstr = ''.join([char for char in name if char not in vowels])
#     print("Output:", newstr)

# main()
