def main():
    print(get_str("Name:"))


def get_str(prompt):
    names = []

    while True:
        try:
            names.append(input(prompt))
        except EOFError:
            return names

main()
