def main():
    text = input("Say Something! ")
    print(f"{convert(text)}")


def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")


main()
