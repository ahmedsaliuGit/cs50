import sys
import csv

def main():
    is_valid = validate_input(sys.argv)

    if is_valid == True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(is_valid)

    print(reader.reader())

def validate_input(arguments):
    size = len(arguments[1:])

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"
    elif not arguments[1].endswith(".csv"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
