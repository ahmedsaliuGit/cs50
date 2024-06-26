import sys
import csv

def main():
    is_valid = validate_input(sys.argv)
    contents = []

    if is_valid == True:
        try:
            with open(sys.argv[1], "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == "name":
                        continue
                    split_col = row[0].split(",")
                    contents.append([split_col[0], split_col[1], row[1]])

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(is_valid)

    print(contents)

def validate_input(arguments):
    size = len(arguments[1:])

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    # elif not arguments[1].endswith(".csv"):
        # return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
