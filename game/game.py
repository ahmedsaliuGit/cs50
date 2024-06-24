from random import randint

def main():
    level = get_input("Level: ")

    rand_num = randint(1, level)


    while True:
        guess = get_input("Guess: ")
        print(guess, rand_num)
        if rand_num == guess:
            print("Just right!")
            break
        elif rand_num < guess:
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
