import requests
import argparse
import json

    """
        This program gives you opportunity to get information of an IP address.
    """
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--ipaddress", help="IP address to track")

    args = parser.parse_args()

    ip = args.ipaddress

    url = "http://ip-api.com/json/"+ip

    # http://ip-api.com/json/{ip_address}

    response = requests.get(url)

    data = json.loads(response.content)

    print("\t[+] IP\t\t\t", data["query"])
    print("\t[+] CITY\t\t", data["city"])
    print("\t[+] ISP\t\t\t", data["isp"])
    print("\t[+] LOC\t\t\t", data["country"])
    print("\t[+] REG\t\t\t", data["regionName"])
    print("\t[+] TIME\t\t", data["timezone"])
    print("\t[+] ZIP\t\t\t", data["zip"])
    print("\t[+] LAT\t\t\t", data["lat"])
    print("\t[+] LON\t\t\t", data["lon"])