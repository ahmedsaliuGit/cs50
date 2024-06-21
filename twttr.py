output = ""

answer = input("Input: ")

for char in answer:
    if char.title() == "A" or char.title() == "E" or char.title() == "I" or char.title() == "O" or char.title() == "U":
        output += ""
    else:
        output += char

print("Output:", output)
