import random


def main():
    ...


def get_level(prompt):
    while True:
        try:
            num = int(input(prompt))

            if num <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return num


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
