import sys


def main():
    is_valid = validate_input(sys.argv)

    print(is_valid)


def validate_input(arguments):
    size = len(arguments[1:])

    jpg1 = arguments[1].lower().endswith("jpg")
    jpg2 = arguments[2].lower().endswith("jpg")
    jpeg1 = arguments[1].lower().endswith("jpeg")
    jpeg2 = arguments[2].lower().endswith("jpeg")
    png1 = arguments[1].lower().endswith("png")
    png2 = arguments[2].lower().endswith("png")

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    elif not arguments[1].lower().endswith((".jpg", ".jpeg", ".png")) and not arguments[2].lower().endswith((".jpg", ".jpeg", ".png")):
        return "Invalid input"
    elif jpg1 != jpg2 or jpeg1 != jpeg2 or png1 != png2:
        return "Input and output have different extensions"

    return True


if __name__ == "__main__":
    main()
