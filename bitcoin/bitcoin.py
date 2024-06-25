import sys
import requests

try:
    if len(sys.argv) > 1 and (sys.argv[1].isnumeric() or float(sys.argv[1])):

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        bpi = response.json()

        print("${:,.4f}".format(float(sys.argv[1]) * bpi["bpi"]["USD"]["rate_float"]))
    else:
         sys.exit("Missing command-line argument")
except requests.RequestException:
    print("Network error")
except ValueError:
    sys.exit("Missing command-line argument")
