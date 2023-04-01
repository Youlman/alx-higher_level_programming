#!/usr/bin/python3
""" sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
using package requests"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    req = requests.post(url, data)
    print(req.text)
