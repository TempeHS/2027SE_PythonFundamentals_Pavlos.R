import sys
import pyfiglet import figlet
figlet = Figlet()

def main():

    if len(sys.argv) == 0:



    elif len(sys.argv) == 2:
        font(sys.argv[2])



def font(f):
    figlet.setFont(font=f)  