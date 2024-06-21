output = ""
vowels = {"A": True, "E": True, "I": True, "O": True, "U": True, "a": True, "e": True, "i": True, "o": True, "u": True}

answer = input("Input: ")

for char in answer:
    if char.title() == "A" or char.title() == "E" or char.title() == "I" or char.title() == "O" or char.title() == "U":
        output += ""
    else:
        output += char

print("Output:", output)
