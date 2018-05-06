from HTMLParser import HTMLParser

import urllib2

from bs4 import BeautifulSoup

download_base = "https://builder.blender.org"

links_page = "https://builder.blender.org/download"

page = urllib2.urlopen(links_page)

soup = BeautifulSoup(page, 'html.parser')

tables = soup.findAll('table', attrs={'class': 'table table-striped table-hover box'})

for table in tables:
    anchors = table.findAll('a')
    for anchor in anchors:
        print "Downloading", anchor.attrs['href']
        download_link = download_base+anchor.attrs['href']
        dl = urllib2.urlopen(download_link)
        dest_path = os.path.basename(anchor.attrs['href'])
        with open(dest_path, 'wb') as output:
            output.write(dl.read())
