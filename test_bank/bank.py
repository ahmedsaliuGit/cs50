def main():
    phrase = input("Greeting: ")

    phrase = phrase.lower().replace(" ","")
    print(phrase)
    print(value(phrase))

def value(greeting):
    if not greeting.find("hello"):
        return "$0"

    elif greeting[0] == "h":
        return "$20"

    else:
        return "$100"


if __name__ == "__main__":
    main()
