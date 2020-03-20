#!/usr/bin/env python3

import urllib.request

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    print(htmlstr)
