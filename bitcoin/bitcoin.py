import sys
import requests
import locale

locale.setlocale(locale.LC_ALL, '')

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        bpi = response.json()

        print(locale.format("%.4f", float(sys.argv[1]) * bpi["bpi"]["USD"]["rate_float"]), grouping=True)
    except requests.RequestException:
        print("Network error")
else:
    sys.exit("Missing command-line argument")
