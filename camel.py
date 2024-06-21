name = input("What's your name? ")

output = ''

for char in name:
    if char.istitle():
        output = output + '_' + char.lower()
    else:
        output = output + char

print(output.lstrip('_'))
