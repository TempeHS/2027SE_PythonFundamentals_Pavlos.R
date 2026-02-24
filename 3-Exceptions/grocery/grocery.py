lis = {}
seen = set()
prin = {}


def main():

    while True:
        try:
            x = input("What is your item? ").title()
            if x not in lis:
                lis.update({x: 1})
            else:
                lis[x] += 1
        except EOFError:
            new_lis = dict(sorted(lis.items(), key=lambda item: item[0]))
            print(end="\n")
            for i in new_lis:
                i = i.title()
                print(new_lis[i], end=" ")
                print(i, end="\n")
            break


main()
