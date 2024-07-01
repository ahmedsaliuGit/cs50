import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.\d{1,3}\.\d{1,3}$", ip):
        print(matches)
        if 0 < matches.group(0) > 255 or 0 < matches.group(1) > 255:

        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
