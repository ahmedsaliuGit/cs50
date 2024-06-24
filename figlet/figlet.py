import sys
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()

cmd_argv = sys.argv

if len(cmd_argv) != 0:
    sys.exit()
elif len(cmd_argv[1:]) == 2:
    if cmd_argv[1] != "-f" or cmd_argv[1] != "--font":
        sys.exit("Error: flag is not available")

    if cmd_argv[2] not in fonts:
        sys.exit("Error: font does not exist.")

    


