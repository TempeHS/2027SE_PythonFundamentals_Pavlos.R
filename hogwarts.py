students = [
    {"Name": "Hermoine", "House": "Gryffindor", "Patronus": "Otter"},
    {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
    {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Russel Terrier"},
    {"Name": "Draco", "House": "Slytherin", "Patronus": None},
]


def main():

    for student in students:
        print(student["Name"], student["House"], student["Patronus"], sep=", ")


main()
