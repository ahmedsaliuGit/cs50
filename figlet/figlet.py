import sys
from random import randint
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

cmd_argv = sys.argv
print(len(cmd_argv))
if len(cmd_argv[1:]) == 0:
    figlet.setFont(font=fonts[randint(0, len(fonts))])
elif len(cmd_argv[1:]) == 2:

    if cmd_argv[1] != "-f" and cmd_argv[1] != "--font":
        sys.exit("Invalid usage")

    if cmd_argv[2] not in fonts:
        sys.exit("Invalid usage")

    figlet.setFont(font=cmd_argv[2])

user_str = input("Input: ")

print("Output: ")
print(figlet.renderText(user_str))


