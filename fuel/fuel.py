def main():
    print(get_fraction("Fraction: "))

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
