#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
using package requests """

import requests


if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(req)
        