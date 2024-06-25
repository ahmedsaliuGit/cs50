import sys
import requests

if len(sys.argv) > 1 or sys.argv[1].isnumeric():
    try:
        ...
    except requests.RequestException:
        ...
else:
    sys.exit("Missing command-line argument")
