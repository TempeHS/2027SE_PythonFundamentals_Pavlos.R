import sys
import csv


def main():
    try:
        command_line_check()
        with open(sys.argv[1]) as file:
            with open(sys.argv[2], "w") as file2:
                csvwrite = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                csvwrite.writerow({"first": "first", "last": "last", "house": "house"})
            csvfile = csv.reader(file)
            for row in csvfile:
                try:
                    last_name, first_name = row[0].split(", ")
                    house = row[1]
                except ValueError:
                    continue
                with open(sys.argv[2], "a") as file2:
                    fieldnames = ["first", "last", "house"]
                    csvwrite = csv.DictWriter(file2, fieldnames=fieldnames)
                    csvwrite.writerow(
                        {"first": first_name, "last": last_name, "house": house}
                    )

    except (IndexError, FileNotFoundError):
        sys.exit()


def command_line_check():
    if len(sys.argv) > 3:
        print("Too Long!")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too Short!")
        sys.exit()
    elif sys.argv[1].endswith(".csv") != True or sys.argv[2].endswith(".csv") != True:
        print("Not a .csv!")
        sys.exit()


main()
