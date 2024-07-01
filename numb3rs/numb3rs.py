import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        if 0 < int(matches[1]) > 255 or 0 < int(matches[2]) > 255 or 0 < int(matches[3]) > 255 or 0 < int(matches[4]) > 255:
            return "Invalid"

        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
