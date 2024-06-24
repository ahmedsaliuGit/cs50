import sys
from random import randint
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

cmd_argv = sys.argv

if len(cmd_argv) == 0:
    figlet.setFont(font=fonts[randin(0, len(fonts))])
elif len(cmd_argv[1:]) == 2:
    print(cmd_argv[1] != "-f")
    if cmd_argv[1] != "-f" or cmd_argv[1] != "--font":
        sys.exit("Error: flag is not available")

    if cmd_argv[2] not in fonts:
        sys.exit("Error: font does not exist.")

    figlet.setFont(font=cmd_argv[2])

user_str = input("Input: ")

print("Output: ")
print(figlet.renderText(user_str))


