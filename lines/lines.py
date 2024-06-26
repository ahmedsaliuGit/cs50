import sys

def main():
    if validate_input() == True:
        

def validate_input():
    size = len(sys.argv[1:])

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"
    elif not sys.argv[1].endswith(".py"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
