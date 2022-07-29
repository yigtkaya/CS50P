import requests
import sys

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def main():
    try:
        if not isfloat(sys.argv[1]):
            sys.exit('Command-line argument is not a number')
    except IndexError:
        sys.exit('Missing command-line argument')

    result = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = result.json()
    btc_value = float(result['bpi']['USD']['rate_float'])
    btc_value = btc_value * float(sys.argv[1])
    print(f"${btc_value:,.4f}")

main()