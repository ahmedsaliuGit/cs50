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
        digits = ''

        for i in range(len(s)):
            char = s[i]

            if char in string.punctuation:
                return False

            if digits == '' and char.isnumeric():
                digits += s[i:len(s)]
                print(digits)
                if digits.isdigit():
                    continue
                else:
                    return False

                if digits[0] == '0':
                    return False

    return True

main()
