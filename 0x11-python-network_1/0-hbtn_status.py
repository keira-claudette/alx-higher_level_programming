#!/usr/bin/python3

""" Fetches url"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print("Body responses:")
    print("\t- type:".format(type(response.read())))
    print('\t- content: {}'.format(response.read()))
    print("\t- utf8 content: {}".format(response.read().decode("utf-8", "replace")))
    # print(html)
