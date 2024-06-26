import sys
def main():

    
def validate_input(arguments):
    size = len(arguments[1:])

    if size != 1:
        if size < 1:
            return "Too few command-line arguments"
        elif size > 1:
            return "Too many command-line arguments"
    elif not arguments[1].endswith(".py"):
        return "Not a Python file"

    return True

if __name__ == "__main__":
    main()
