import sqlite3
import urllib2

f = urllib2.urlopen('https://www.ebay-kleinanzeigen.de/s-zu-verschenken/berlin/c192l3331')
page = f.read()

print page
