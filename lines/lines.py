import sys

def main():
    print(validate_input())

def validate_input():
    size = len(sys.argv)

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"

    return True

if __name__ == "__main__":
    main()
