def main():
    fraction = get_fraction("Fraction: ")

    res = (fraction[0] / fraction[1]) * 100

    if res < 1:
        print("E")

    if res >= 99:
        print("F")

    print(f"{res}%")

def get_fraction(prompt):
    while True:
        try:
            x_y = input(prompt).split("/")

            if len(x_y) != 2:
                raise IndexError("List index out of range.")

            x = int(x_y[0])

            y = int(x_y[1])

            if y == 0:
                raise ValueError()

            if x > y:
                raise ValueError()

            return [x, y]
        except ValueError:
            pass
        except IndexError:
            pass

main()
