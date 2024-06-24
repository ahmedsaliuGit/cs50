from random import randint

def main():
    level = get_input("Level: ")

    rand_num = randint(1, level)

    guess = get_input("Guess: ")

    

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
