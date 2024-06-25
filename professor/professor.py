import random


def main():
    level = get_level("Level: ")
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        ans = get_level(f"{x} + {y} = ")

        if ans == x + y:
            score += 1
            continue
        else:
            error = 0

            while error < 3:
                print("EEE")

                ans = get_level(f"{x} + {y} = ")

                if ans == x + y:
                    break

                error += 1

            if error == 3:
                print(f"{x} + {y} = {x + y}")

    print("Score:", score)


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
    elif level == 3:
        return (random.randint(100, 999))
    else:
        raise ValueError


if __name__ == "__main__":
    main()
