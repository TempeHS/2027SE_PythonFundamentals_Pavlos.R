import emoji


def main():

    text = input("Say Something!")

    print(emoji.emojize(text, language="alias"))


main()
