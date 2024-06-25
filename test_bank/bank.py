def main():
    phrase = input("Greeting: ")

    print(value(phrase.lower().replace(" ","")))

def value(greeting):
    if not greeting.find("hello"):
        return "$0"

    elif greeting[0] == "h":
        return "$20"

    else:
        return "$100"


if __name__ == "__main__":
    main()
