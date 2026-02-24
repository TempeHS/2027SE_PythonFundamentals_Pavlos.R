lis = []


def main():

    while True:
        try:
            lis.append(input("What is your item? "))
        except EOFError:
            lis.sort()
            for i in lis:
                i = i.title()
                print(i)
            break


main()
