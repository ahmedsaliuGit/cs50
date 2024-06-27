import sys
import os
from PIL import Image, ImageOps

def main():
    is_valid = validate_input(sys.argv)

    if is_valid == True:
        try:
            with Image.open(sys.argv[1]) as image:
                shirt = Image.open("shirt.png")
                size = shirt.size

                fit_image = ImageOps.fit(image, size)

                fit_image.paste(shirt, shirt).save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit(is_valid)


def validate_input(arguments):
    size = len(arguments[1:])

    if size != 2:
        if size < 2:
            return "Too few command-line arguments"
        elif size > 2:
            return "Too many command-line arguments"
    elif not arguments[1].lower().endswith((".jpg", ".jpeg", ".png")) and not arguments[2].lower().endswith((".jpg", ".jpeg", ".png")):
        return "Invalid input"
    elif os.path.split(arguments[1].lower())[1] != os.path.split(arguments[2].lower())[1]:
        print(os.path.split(arguments[1].lower())[1], os.path.split(arguments[2].lower())[1])
        return "Input and output have different extensions"

    return True


if __name__ == "__main__":
    main()
