import sys
import requests

try:
    bitcoins = float(sys.argv[1])
except (ValueError, IndexError):
    sys.exit("Please enter a valid number of bitcoins to buy as a command-line argument.")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    price = data["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    sys.exit("Unable to retrieve Bitcoin price data from API.")

cost = bitcoins * price
print(f"The current cost of {bitcoins:,.8f} Bitcoins is ${cost:,.4f}.")
