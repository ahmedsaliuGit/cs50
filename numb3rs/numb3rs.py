import re
import sys


def main():
    validate(input("IPv4 Address: "))


def validate(ip):
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
