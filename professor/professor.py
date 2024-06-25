import random


def main():
    level = get_input("Level: ")
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        ans = get_input(f"{x} + {y} = ")

        if ans == x + y:
            continue
        else:
            error = 0

            while error < 3:
                print("EEE")

                

                error += 1


def get_level(prompt):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            if prompt == "Level: ":
                pass
            else:
                return "EEE"
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
