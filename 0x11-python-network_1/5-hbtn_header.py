#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status
using package requests """

import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get("X-Request-Id"))
