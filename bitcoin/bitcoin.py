import sys
import requests

if len(sys.argv) > 1 or sys.argv[1].isnumeric():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        bpi = response.json()
    except requests.RequestException:
        print("Network error")
else:
    sys.exit("Missing command-line argument")
