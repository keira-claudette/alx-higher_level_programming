#!/usr/bin/python3

""" Fetches url"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print("\t- {}".format(response.read()))
    # print(html)
