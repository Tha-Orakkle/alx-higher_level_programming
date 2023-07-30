#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    data = resp.read()
    result = "Body response:\n\t- type: {}\n\t- content: {}\n\t"
    result += "- utf8 content: {}"
    print(result.format(type(data), data, data.decode("utf-8")))

