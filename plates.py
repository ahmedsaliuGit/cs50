import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif " " in s:
        return False
    else:
        for char in s:
            if char in string.punctuation:
                return False

    return True

main()
