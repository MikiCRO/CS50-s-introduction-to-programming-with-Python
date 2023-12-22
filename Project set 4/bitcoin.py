import requests
import sys
import json

def main():
    if len(sys.argv) !=2:
        sys.exit("Missing command line argument")
        
    try:
        quantities=float(sys.argv[1])
    except ValueError:
        sys.exit("command line argument is not valid")
        
    try:
        response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Connection cannot be established")
        
    else:
        bitcoin=response.json()
        price=bitcoin["bpi"]["USD"]["rate"].replace(",","")
        rate=quantities * float(price)
        print(f"${rate:,.4f}")
        
main()
