import sys
from random import randint

def main():
    level = get_input("Level: ")

    rand_num = randint(1, level)


    while True:
        guess = get_input("Guess: ")

        if rand_num == guess:
            print("Just right!")
            sys.exit()
        elif guess < rand_num:
            print("Too small!")
        else:
            print("Too large!")

def get_input(prompt):
    while True:
        try:
            num = int(input(prompt))

            if num <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return num

main()
