#!/usr/bin/python3
""" sends a POST request to the passed URL with the email 
as a parameter, and displays the body of the response """

import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    with urllib.request.urlopen(req, data) as response:
        body = response.read()
        print(body)
