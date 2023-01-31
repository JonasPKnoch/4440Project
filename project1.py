import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd import *
url = sys.argv[1]

# Your code to modify the URL goes here!

parsedUrl = urlparse(url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
