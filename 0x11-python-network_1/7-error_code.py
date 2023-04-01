#!/usr/bin/python3
"""Sends a request to the URL and displays
the body of the response using pakage requests"""

import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if (req.status_code >= 400):
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
