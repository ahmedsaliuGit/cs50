import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d{1,3}", ip)


if __name__ == "__main__":
    main()
