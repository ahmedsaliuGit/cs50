import random


def main():
    ...


def get_level(prompt):
    while True:
        try:
            num = int(input(prompt))

            if num <= 0:
                raise ValueError

            if num 
        except ValueError:
            pass
        else:
            return num


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return (random.randint(100, 999))


if __name__ == "__main__":
    main()
