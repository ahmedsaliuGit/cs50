def main():
    print(get_fraction("Fraction: "))
def get_fraction(prompt):
    while True:
        try:
            x_y = input(prompt).split("/")

            if len(x_y) != 2:
                raise

            x = int(x_y[0])

            y = int(x_y[1])

            return [x, y]
        except ValueError:
            pass

main()
