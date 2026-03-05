import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            bitcoin = float(sys.argv[1])
        except ValueError:
            sys.exit()
        else:
            bitcoin_convert(bitcoin)

    else:
        sys.exit()


def bitcoin_convert(bitcoin):
    try:
        lis = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

        print(lis.json())
    except requests.RequestException:
        print("Error")


main()
