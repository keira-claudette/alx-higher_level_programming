#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of
 the response (decoded in utf-8)."""

import sys
import urllib.request
import urllib.error

req = urllib.request.Request(sys.argv[1])
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print("Error code: {}".format(e.code))

if __name__ == "main":
    pass
