import random


def main():

    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("What Level Do You Choose? "))

        except ValueError:
            continue

        else:
            if level <= 0 or level > 3:
                continue
            else:
                return level


def generate_integer(level):




if __name__ == "__main__":
    main()
