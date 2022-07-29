import random
import sys

def level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level >= 1:
                selected = random.randint(1,level)
                guess(selected)
                break
        except (ValueError,TypeError):
            continue


def guess(generated_number):
    while True:
        guess = input("Guess: ").strip()
        try:
            if guess.isdigit():
                guess = int(guess)
                if guess > generated_number:
                    print("Too large!")
                elif guess < generated_number:
                    print("Too small!")
                else:
                    sys.exit("Just right!")
        except EOFError:
            break

level()
