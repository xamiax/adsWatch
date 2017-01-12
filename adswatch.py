#import sqlite3
import urllib2
import StringIO

#contents = output.getvalue()
#print contents
#output.close()


f = urllib2.urlopen('https://www.ebay-kleinanzeigen.de/s-zu-verschenken/berlin/c192l3331')
counter = 0
#page = f.read()

for line in f:
  thisline = line
  if '<ul id="srchrslt-adtable"' in thisline:
    adshtml = StringIO.StringIO()
    break

for line in f:
  if '<ul' in line:
    counter += 1
  if '</ul' in line:
    if counter == 0:
      break
    else:
      counter -= 1
  adshtml.write(line)

ads = []

for line in adshtml:
  if '<li' in line:
    counter += 1





print adshtml.getvalue()
#print adshtml



"""
item:
  id
  img
  title
  subtitle
  plz
  bezirk
  timestamp

-    <li class="ad-listitem lazyload-item   ">
            <article class="aditem" data-adid="583452920">
-                <section class="aditem-image">
                    <div  data-href="/s-anzeige/schrankwand-mit-beleuchtung-zu-verschenken/583452920-192-3409" data-imgsrc="https://i.ebayimg.com/00/s/MTAyNFg1NzU=/z/a6EAAOSwt5hYd4tA/$_9.JPG" data-imgtitle="Schrankwand mit Beleuchtung zu verschenken Berlin - Tempelhof Vorschau" class="imagebox srpimagebox"></div>
-                                </section>
-                <section class="aditem-main">
                    <h2 class="text-module-begin"><a name="583452920" href="/s-anzeige/schrankwand-mit-beleuchtung-zu-verschenken/583452920-192-3409">Schrankwand mit Beleuchtung zu verschenken</a></h2>
                    <p>Lieferung gegen Aufpreis innerhalb spandau moeglich</p>


-                    <p class="text-module-end">
-                    </p>

-                    </section>
-                <section class="aditem-details">
                    12099<br>
                    Tempelhof<br>
-                    </section>
-                <section class="aditem-addon">
                    Heute, 16:30</section>
-            </article>
-        </li>
"""
