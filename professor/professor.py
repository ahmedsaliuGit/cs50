import random


def main():
    level = get_level("Level: ")
    print(generate_integer(level))


def get_level(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            pass
        else:
            if prompt == "Level: ":
                if num == 1 or num == 2 or num == 3:
                    return num
                else:
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
