def main():
    text = input("What's your tweet? ")
    for i in text:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print(end="")
        else:
            print(i, end="")
    print()


main()
