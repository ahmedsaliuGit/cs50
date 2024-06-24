def main():
    names = get_str("Name: ")
    output = "Adieu, adieu, to "
    n = len(names)

    for i in range(n):
        name = names[i]
        output += name

        if i == n - 2:
            output += " and "
        elif i > 0 and i < n - 1:
            output += ", "

    print(output)


def get_str(prompt):
    names = []

    while True:
        try:
            names.append(input(prompt))
        except EOFError:
            return names

main()
