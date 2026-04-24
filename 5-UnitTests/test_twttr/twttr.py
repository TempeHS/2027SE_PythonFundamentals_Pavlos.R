def main():
    text = input("What's your tweet? ")
    for i in text:
        print(f"{shorten(text)}", end="")
    print()


def shorten(text):
    new_text = str()
    for i in text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            continue
        else:
            new_text += i

    return new_text


if __name__ == "__main__":
    main()
