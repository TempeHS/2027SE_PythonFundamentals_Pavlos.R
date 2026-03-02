import sys
import random
from pyfiglet import Figlet


figlet = Figlet()


def main():

    if len(sys.argv) == 1:

        rand_font()

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font(sys.argv[2])

    else:
        print("invalid usage")
        sys.exit()


def font(f):
    if f in figlet.getFonts():

        figlet.setFont(font=f)
        prompt()
    else:
        print("invalid")


def rand_font():

    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    prompt()


def prompt():

    text = input("What would you like to say? \n")
    print(figlet.renderText(text))


main()
