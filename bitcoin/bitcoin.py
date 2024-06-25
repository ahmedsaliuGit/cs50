import sys
import requests

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        bpi = response.json()

        print(f"${(float(sys.argv[1]) * bpi["bpi"]["USD"]["rate_float"]):,.4f}")
    except requests.RequestException:
        print("Network error")
else:
    sys.exit("Missing command-line argument")
