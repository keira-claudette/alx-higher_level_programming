#!/bin/bash
# takes a URL as argument, sends a GET request to the URL, and displays
# the body of the response
curl -s -X GET "$1" -L
