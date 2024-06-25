
import sys
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

            while ans != x + y:
                print("EEE")

                ans = get_level(f"{x} + {y} = ")

                if error >= 3:
                    sys.exit(str(x) + " + " + str(y) + " = " + str(x + y))

                error += 1

    print("Score: ", score)


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
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return (random.randint(100, 999))
    except:
        raise ValueError


main()
