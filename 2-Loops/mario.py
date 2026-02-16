layouts = [
    {"x": 1, "y": 0},
    {"x": 1, "y": 1},
    {"x": 1, "y": 2},
    {"x": 1, "y": 3},
]


def main():
    printSquare(5)


def printSquare(size):

    row = 0
    column = 0
    for row in range(size):
        for layout in layouts:
            if row == layout["x"]:
                for column in range(size):
                    if column == layout["y"]:
                        print("#", end="")
                    else:
                        print(" ", end="")
            else:
                for column in range(size):
                    print(" ", end="")
            print(" ", end="\n")


main()
