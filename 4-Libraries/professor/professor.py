import random
import sys


def main():

    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("What Level Do You Choose? "))

        except ValueError:
            continue

        else:
            if level <= 0 or level > 3:
                continue
            else:
                return level


def generate_integer(level):
    question_num = 1
    lives = 3
    score = 0
    while question_num <= 10:
        correct = False

        num_1 = random.randint(1, (1 * pow(10, level)) - 1)
        num_2 = random.randint(1, (1 * pow(10, level)) - 1)
        answer = num_1 + num_2
        while correct == False:
            if lives <= 0:
                print(f"Your score was: {score}")
                sys.exit()
            print(f"What is {num_1} + {num_2}?")
            try:
                user_answer = int(input())
            except ValueError:
                continue
            else:
                if user_answer != answer:
                    lives -= 1
                    print("EEE")
                else:
                    correct = True
                    question_num += 1
                    score += 1
    print(score)
    sys.exit()


if __name__ == "__main__":
    main()
