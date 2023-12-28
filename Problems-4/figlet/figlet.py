# Frank, Ian and Glen’s Letters
# FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

#  _ _ _          _   _     _
# | (_) | _____  | |_| |__ (_)___
# | | | |/ / _ \ | __| '_ \| / __|
# | | |   <  __/ | |_| | | | \__ \
# |_|_|_|\_\___|  \__|_| |_|_|___/
# Among the fonts supported by FIGlet are those at http://www.figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

# Hints
# You can install pyfiglet with:
# pip install pyfiglet
# The documentation for pyfiglet isn’t very clear, but you can use the module as follows:
# from pyfiglet import Figlet

# figlet = Figlet()
# You can then get a list of available fonts with code like this:

# figlet.getFonts()
# You can set the font with code like this, wherein f is the font’s name as a str:

# figlet.setFont(font=f)
# And you can output text in that font with code like this, wherein s is that text as a str:

# print(figlet.renderText(s))
# Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    avto = argv_check(sys.argv, figlet)
    control(avto, figlet)


def argv_check(av, fig):
    if len(av) == 3:
        if av[1] == "--font" or av[1] == "-f":
            if font_check(av[2], fig):
                return av[2]
    sys.exit("Invalid usage")


def font_check(avto, fig):
    fonts = get_fonts(fig)
    if avto in fonts:
        return True
    else:
        return False


def control(avto, fig):
    text = get_in()
    get_out(text, avto, fig)


def get_in():
    return input("Input: ")


def get_out(text, font, fig):
    fig.setFont(font=font)
    print(fig.renderText(text))


def get_fonts(figlet):
    return figlet.getFonts()


if __name__ == "__main__":
    main()
