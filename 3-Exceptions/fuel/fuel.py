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


main()
