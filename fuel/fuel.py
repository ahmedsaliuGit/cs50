def main():
    print(get_fraction("Fraction: "))
def get_fraction(prompt):
    while True:
        try:
            x_y = input(prompt).split("/")

            x = int(x_y[0])

            y = int(x_y[1])
        except ValueError:
            pass

main()
