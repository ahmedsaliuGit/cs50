def main():
    print(get_fraction("Fraction: "))
def get_fraction(prompt):
    while True:
        try:
            x_y = input(prompt).split("/")

            return x_y
        except ValueError:
            pass

main()
