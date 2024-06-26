import sys

def main():
    lines_code =0

    if validate_input(sys.argv) == True:
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.strip().startswith("#") and not line.isspace():
                        lines_code += 1

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(validate_input())

    print(lines_code)

def validate_input(arguments):
    size = len(arguments[1:])

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"
    elif not arguments[1].endswith(".py"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
