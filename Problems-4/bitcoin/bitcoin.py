import requests
import sys


def main():
    if len(sys.argv) == 2:
        control(sys.argv[1])
    else:
        sys.exit("Missing command-line argument")


def control(a):
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
        btc_price = get_price(r)
        btc = float(a)
        get_out(btc_price * btc)

    except requests.RequestException:
        pass
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_price(r):
    return float(r["bpi"]["USD"]["rate_float"])


def get_out(amount):
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
