#!/usr/bin/python3
"""Sends a request to the URL and displays
the body of the response using pakage requests"""

import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(type(req.status_code))
