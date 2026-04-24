def main():
    x = int(input("What number would you like to square?"))
    assert square(x) == 3


def square(n):
    return n * n


if __name__ == "__main__":
    main()
