import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'^<iframe .* src="https?://(?:www\.)?youtube\.com/embed/(\w)+" .*></iframe>$', s)



if __name__ == "__main__":
    main()
