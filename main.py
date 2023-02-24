import random


def main():
    print("=" * 30)
    print("Welcome to the guessing game")
    print("=" * 30)

    random_number = random.randint(1, 2)

    guess = input("Guess the integer number: ")

    if not guess.isdigit():
        print("You need put a number!")
        return

    number = int(guess)

    if number == random_number:
        print("You got it!")
    else:
        print("You are wrong")

    print(random_number)


if __name__ == "__main__":
    main()
