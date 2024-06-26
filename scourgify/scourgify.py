import sys
import csv


def validate_input(arguments):
    size = len(arguments[1:])

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    elif not arguments[1].endswith(".csv"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
