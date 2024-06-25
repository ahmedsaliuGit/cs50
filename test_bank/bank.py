def main():
    phrase = input("Greeting: ")

    print(value(phrase))

def value(greeting):
    b = greeting.lower().replace(" ","")

    if not b.find("hello"):
        return "$0"

    elif b[0] == "h":
        return "$20"

    else:
        return "$100"


if __name__ == "__main__":
    main()
