def main():
    answer = input("Input: ")

    print("Output:", shorten)


def shorten(word):
    output = ""

    for char in answer:
        if char.title() == "A" or char.title() == "E" or char.title() == "I" or char.title() == "O" or char.title() == "U":
            output += ""
        else:
            output += char

    return output


if __name__ == "__main__":
    main()
