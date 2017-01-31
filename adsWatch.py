import sqlite3
import urllib2
from lxml import etree

xml = '<a xmlns="test"><b xmlns="test"/></a>'

url = 'https://www.ebay-kleinanzeigen.de/s-zu-verschenken/berlin/c192l3331'
request = urllib2.Request(url)
f = urllib2.urlopen(request)
html = f.read()
html = html.replace('\n', '')

#print repr(html)

root = etree.fromstring(xml)

















#f = urllib2.urlopen('https://www.ebay-kleinanzeigen.de/s-zu-verschenken/berlin/c192l3331')
#fcopy = f
#page = fcopy.read()
#print page

#parser = ET.XMLParser(encoding="utf-8")
#tree = ET.fromstring(page, parser=parser)

