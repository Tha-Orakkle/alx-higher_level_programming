#!/usr/bin/python3
"""
sends a request to a url and displays the value of
the 'X-Request-Id' variable found in the header response.
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
