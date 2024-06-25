import sys
import requests

if len(sys.argv) > 1 and sys.argv[1].isdigit():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        bpi = response.json()

        print("${:,.4f}".format(float(sys.argv[1]) * bpi["bpi"]["USD"]["rate_float"]))
    except requests.RequestException:
        print("Network error")
else:
    sys.exit("Missing command-line argument")
