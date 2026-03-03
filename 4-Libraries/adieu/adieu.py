import inflect

p = inflect.engine()

names = []


def main():

    while True:

        try:
            name = input("State a name. ")
            names.append(name)
            continue
        except (KeyboardInterrupt, EOFError):
            break

    output_print()


def output_print():
    joined_output = p.join(names)
    print(f"Adieu, Adieu, to {joined_output}")


main()
