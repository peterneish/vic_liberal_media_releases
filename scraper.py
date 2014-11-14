# This is a template for a Python scraper on Morph (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://vic.liberal.org.au")
data
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
for li in root.cssselect("li[class='media-releases-item']"):
  title = li.cssselect("h4")[0].text_content()
  link  = li.cssselect("a")[0].attrib('href')
  
  # # Write out to the sqlite database using scraperwiki library
  scraperwiki.sqlite.save(unique_keys=['title'], data={"title": title, "link": link})

