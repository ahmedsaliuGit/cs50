import sys
import csv

def main():
    is_valid = validate_input(sys.argv)

    print(is_valid)

def validate_input(arguments):
    size = len(arguments[1:])

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    elif not arguments[1].lower().endswith((".jpg", ".jpeg", ".png")) and not arguments[2].lower().endswith((".jpg", ".jpeg", ".png")):
        return "Invalid input"
    elif arguments[1].lower().endswith("jpg") != arguments[2].lower().endswith("jpg"):
        return "Input and output have different extensions"

    return True

if __name__ == "__main__":
    main()
