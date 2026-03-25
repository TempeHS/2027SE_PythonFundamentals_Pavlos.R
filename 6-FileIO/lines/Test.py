import sys


def main():
    try:
        with open(sys.argv[1], "r") as file:
            if len(sys.argv) > 2:
                sys.exit
            lines = file.readlines()
            line_count = len(lines)
    except IndexError:
        sys.exit


main()
