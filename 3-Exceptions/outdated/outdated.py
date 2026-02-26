months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        text = input("Date? ")
        try:

            a, b, c = text.split(sep="/")
        except ValueError:
            try:
                a, c = text.split(sep=",")
            except ValueError:
                continue
            else:
                try:
                    a, b = a.split(sep=" ")
                except ValueError:
                    continue
                else:
                    words(a, b, c)
                    break
        else:
            numbers(a, b, c)
            break


def words(a, b, c):
    try:
        a = str(months.index(a.title()) + 1)
    except ValueError:
        main()
    else:
        numbers(a, b, c)


def numbers(a, b, c):

    if int(a) <= 12 and int(a) > 0 and int(b) <= 31 and int(b) > 0:
        a = a.rjust(2, "0")
        b = b.rjust(2, "0")
        c = c.rjust(4, "0").removeprefix(" ")
        print(c + "-" + a + "-" + b)
    else:
        main()


main()
