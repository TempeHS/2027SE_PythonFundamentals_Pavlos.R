import sys


def main():
    try:
        with open(sys.argv[1], "r") as file:
            if len(sys.argv) > 2:
                print("Too Long!")
                sys.exit
            elif sys.argv[1].endswith(".py") != True:
                print("Not a .py!")
                sys.exit()
            lines = file.readlines()
            line_count = len(lines)
            print(line_count)
    except (IndexError, FileNotFoundError):
        sys.exit


main()
