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
                    last, first = row[0].split(", ")
                    contents.append([first, last, row[1]])

            with open(sys.argv[2], "w") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(["first", "last", "house"])
                writer.writerows(contents)
        except IOError:
            sys.exit(f"Could not read {sys.argv[1]}")
    else:
        sys.exit(is_valid)

    # print(contents)

def validate_input(arguments):
    size = len(arguments[1:])

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    elif not arguments[1].lower().endswith((".jpg", ".jpeg", ".png")) and not arguments[2].lower().endswith((".jpg", ".jpeg", ".png")):
        return "Input and output have different extensions"

    return True

if __name__ == "__main__":
    main()
