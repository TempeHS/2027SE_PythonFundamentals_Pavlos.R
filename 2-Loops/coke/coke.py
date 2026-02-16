def main():

    amount = int(input("$50c due! "))
    trueAmount = 0
    if amount == 5 or amount == 10 or amount == 25:
        trueAmount = amount
    cokeCost = 50

    while trueAmount < cokeCost:
        if amount == 5 or amount == 10 or amount == 25:
            amount = int(input("You still owe {0}c! ".format(cokeCost - trueAmount)))
            if amount == 5 or amount == 10 or amount == 25:
                trueAmount += amount
        else:
            print("that's an invalid currency amount! ")
            amount = int(input(""))
            if amount == 5 or amount == 10 or amount == 25:
                trueAmount += amount

    print("Thank you, heres your coke! ")


main()
