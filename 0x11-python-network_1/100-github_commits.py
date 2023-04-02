#!/usr/bin/python3
""" Print all commits by: `<sha>: <author name>` using Github API"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])
    req = requests.get(url).json()
    for i in range(10):
        print("{}: {}".format(
            req[i].get("sha"),
            req[i].get("commit").get("author").get("name")))
