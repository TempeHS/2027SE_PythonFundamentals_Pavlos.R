import sys
from tabulate import tabulate
import csv


def main():
    try:
        with open(sys.argv[1], "r") as file:
            if len(sys.argv) > 2:
                print("Too Long!")
                sys.exit()
            elif sys.argv[1].endswith(".csv") != True:
                print("Not a .csv!")
                sys.exit()
            reader = csv.reader(file)

            print(tabulate(reader))
    except (IndexError, FileNotFoundError):
        sys.exit


main()
