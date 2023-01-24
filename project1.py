import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd import *
#url = sys.argv[1]
url = "http://cs4440.eng.utah.edu/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp"
len_m = 8 + len(quote("user=admin&command1=ListFiles&command2=NoOp"))

x = quote("&user=admin&command1=ListFiles&command2=NoOp")
print(quote("&command3=UnlockAllSafes"))

bits = (len_m + len(padding(len_m*8)))*8
print(bits)
h = md5(state="402a574d265dc212ee64970f159575d0", count=bits)
h.update(x)
new_hash = h.hexdigest()
print(new_hash)

modified_url = "http://cs4440.eng.utah.edu/project1/api?token=" + new_hash + "&user=admin&command1=ListFiles&command2=NoOp&command3=UnlockAllSafes"
print(modified_url)

parsedUrl = urlparse(modified_url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())