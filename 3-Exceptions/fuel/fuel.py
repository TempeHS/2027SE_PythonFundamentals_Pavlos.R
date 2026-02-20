def main():

    fract_convert(input("What Is Your Fuel? "))


def fract_convert(fuel):

    x, y = fuel.split("/")
    print(x / y * 100 + "%")


main()
