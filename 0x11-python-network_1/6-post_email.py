#!/usr/bin/python3
""" sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
using package requests"""

import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.post("X-Request-Id", data={"email": sys.argv[2]}))
