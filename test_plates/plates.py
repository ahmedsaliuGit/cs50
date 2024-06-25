import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        return True
    else:
        print("Invalid")
        return False


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s.isdigit():
        return False
    elif " " in s:
        return False
    else:
        digits = ''

        for i in range(len(s)):
            char = s[i]

            if char in string.punctuation:
                return False

            if digits == '' and char.isnumeric():
                digits += s[i:len(s)]

                if digits[0] == '0':
                    return False

                if digits.isdigit():
                    continue
                else:
                    return False

    return True

if __name__ == "__main__":
    main()
