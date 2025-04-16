import urllib.request
import sys

url = "https://books.toscrape.com/"

try:
    with urllib.request.urlopen(url) as doc:
        html = doc.read()
except Exception as e:
    print("Could not open %s" % url, file=sys.stderr)
    print("Error:", e, file=sys.stderr)
