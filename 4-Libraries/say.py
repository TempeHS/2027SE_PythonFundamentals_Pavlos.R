import sys
import cowsay


def main():
    if len(sys.argv) == 2:
        cowsay.trex("Hello, " + sys.argv[1])


main()
