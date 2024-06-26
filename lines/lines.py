import sys

def main():
    lines_code =0

    if validate_input() == True:
        try:
            with open(sys.argv[1]) as file:
                for line in file:
                    if not line.startswith("# ") or not line.startswith("#") or line == " ":
                        lines_code += 1

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(validate_input())

def validate_input():
    size = len(sys.argv[1:])

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"
    elif not sys.argv[1].endswith(".py"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
