def main():
    string = input("Your CamelCasing")
    for i in range(len(string)):
        if string[i].isupper():
            print("_", end="")
        print(string[i].lower(), end="")


main()
