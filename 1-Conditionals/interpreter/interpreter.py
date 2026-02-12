def main():
    one = int(input("what is your first number? "))
    two = input("What is your operator? ")
    three = int(input("what is your second number? "))

    print(f"{calculations(one, two, three)}")


def calculations(x, y, z):

    match y:
        case "+":
            return x + z
        case "-":
            return x - z
        case "*":
            return x * z
        case "/":
            return x / z
        case _:
            return "unknown"


main()
