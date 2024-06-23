def main():
    print(get_fraction("Fraction: "))
def get_fraction(prompt):
    while True:
        try:
            x_y = input(prompt).split("/")
            print(len(x_y))
            if len(x_y) < 2:
                raise IndexError("List index out of range.")

            x = int(x_y[0])

            y = int(x_y[1])

            return [x, y]
        except ValueError:
            pass
        except IndexError:
            pass

main()
