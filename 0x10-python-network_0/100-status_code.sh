#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response
# Read: https://www.journaldev.com/35489/dev-null-in-linux & https://curl.se/docs/manpage.html
curl -sI -w '%{response_code}' "$1" -o /dev/null
