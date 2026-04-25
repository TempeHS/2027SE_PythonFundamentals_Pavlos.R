def main():

    try:

        x, y = input("What Is Your Fuel? ").split("/")
        x = int(x)
        y = int(y)

        text = x / y
    except ValueError:
        main()
    except ZeroDivisionError:
        main()
    else:

        if text < 1 and text > 0:
            print(str(text * 100) + "%")

        elif text == 1:
            print("F")

        elif text == 0:
            print("E")
        else:
            main()


def convert(fract):
    try:

        x, y = fract.split("/")
        x = int(x)
        y = int(y)

        text = x / y
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError
    except AttributeError:
        return AttributeError
    else:
        return fraction(text)


def fraction(text):
    if text < 1 and text > 0:
        return str(text * 100) + "%"

    elif text == 1:
        return "F"

    elif text == 0:
        return "E"
    else:
        return "Failed"


if __name__ == "__main__":
    main()
