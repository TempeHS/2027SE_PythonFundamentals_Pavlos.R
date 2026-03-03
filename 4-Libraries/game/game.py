import random
import sys


def main():

    while True:
        level = None
        try:
            level = int(input("What level? "))

        except ValueError:
            continue

        else:
            if level > 0:
                game(level)

            else:
                continue


def game(n):

    guess = None
    num = random.randint(1, n)

    while guess != num:
        try:
            guess = int(input("What is your guess?"))
        except ValueError:
            continue
        else:
            if guess <= 0:
                continue
            elif guess < num:
                print("Too Small!")
            elif guess > num:
                print("Too Large")
            elif guess == num:
                print("Correct!")
                sys.exit()


main()
